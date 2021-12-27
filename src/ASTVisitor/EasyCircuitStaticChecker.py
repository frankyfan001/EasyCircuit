import copy

from toposort import toposort, CircularDependencyError

from AST.ComponentType import ComponentTypeEnum
from AST.Draw import Draw
from AST.IfThenElse import IfThenElse
from AST.Loop import Loop
from AST.Num import Num
from AST.Output import Output
from AST.Simulate import Simulate
from AST.Var import Var
from ASTVisitor.BaseASTVisitor import BaseASTVisitor
from common.common import get_pos_str
from src.AST.Circuit import Circuit
from src.AST.Component import Component
from src.AST.Connect import Connect
from src.AST.Program import Program


# Static AST Validator
# visit AST nodes and raise exception
class EasyCircuitStaticChecker(BaseASTVisitor):

    def __init__(self):
        self.symbol_table = {}
        self.graph = {}

    def validate(self, program: Program):
        program.accept(self)

    # validate a program
    def visit_program(self, program: Program):
        for statement in program.statements:
            statement.accept(self)

    # validate a circuit
    def visit_circuit(self, circuit: Circuit):
        self.symbol_table[circuit.name] = circuit

        for component in circuit.components:
            component.accept(self)

        # Reset graph before processing connects in circuit.
        self.graph = {}
        for connect in circuit.connects:
            connect.accept(self)
        self.validate_circuit_graph(circuit)

    # validate a circuit by checking properties of a connect graph
    def validate_circuit_graph(self, circuit: Circuit):
        # CIRCUIT currently supports logic gate only.
        try:
            topoli = list(toposort(self.graph))

            if len(circuit.connects) != 3 or \
                    len(topoli) != 3 or len(topoli[0]) != 1 or len(topoli[1]) != 1 or len(topoli[2]) != 2:
                raise Exception(f"At {get_pos_str(circuit)}  "
                                f"CIRCUIT currently supports logic gate only: "
                                f"{circuit.name} does not match the structure of logic gate!")

            output = list(topoli[0])
            if output[0].get_type_enum() != ComponentTypeEnum.OUTPUT:
                raise Exception(f"At {get_pos_str(circuit)}  "
                                f"CIRCUIT currently supports logic gate only: "
                                f"{circuit.name} must have exactly 1 OUTPUT component!")

            logic = list(topoli[1])
            if logic[0].get_type_enum() != ComponentTypeEnum.AND and \
                    logic[0].get_type_enum() != ComponentTypeEnum.OR and \
                    logic[0].get_type_enum() != ComponentTypeEnum.XOR:
                raise Exception(f"At {get_pos_str(circuit)}  "
                                f"CIRCUIT currently supports logic gate only: "
                                f"{circuit.name} must have exactly 1 LOGIC component!")

            inputs = list(topoli[2])
            if (inputs[0].get_type_enum() != ComponentTypeEnum.INPUT and
                inputs[0].get_type_enum() != ComponentTypeEnum.CIRCUIT) or \
                    (inputs[1].get_type_enum() != ComponentTypeEnum.INPUT and
                     inputs[1].get_type_enum() != ComponentTypeEnum.CIRCUIT):
                raise Exception(f"At {get_pos_str(circuit)}  "
                                f"CIRCUIT currently supports logic gate only: "
                                f"{circuit.name} must have exactly 2 INPUT components!")

        except CircularDependencyError:
            raise CircularDependencyError

    # validate a component: put component into symbol table
    def visit_component(self, component: Component):
        self.symbol_table[component.name] = component

    # validate a connect: both from and to needs to be defined
    def visit_connect(self, connect: Connect):
        undefined = connect.connect_from if connect.connect_from not in self.symbol_table \
            else connect.connect_to if connect.connect_to not in self.symbol_table else None
        if undefined:
            raise Exception(f"At {get_pos_str(connect)}  "
                            f"{undefined} is not defined before use!")
        from_comp = self.symbol_table[connect.connect_from]
        to_comp = self.symbol_table[connect.connect_to]

        if from_comp.get_type_enum() == ComponentTypeEnum.CIRCUIT:
            from_comp = copy.deepcopy(from_comp)

        if from_comp not in self.graph:
            self.graph[from_comp] = []

        self.graph[from_comp].append(to_comp)

    # validate a draw statement: the circuit/simualte for drawing should be defined
    def visit_draw(self, draw: Draw):
        if draw.name is not None:
            if draw.name not in self.symbol_table:
                raise Exception(f"At {get_pos_str(draw)}  "
                                f"{draw.name} is not defined before use!")
        else:
            draw.simulate.accept(self)

    # validate a simulate statement: the circuit_id used for simulate should be define
    def visit_simulate(self, simulate: Simulate):
        if simulate.circuit_id not in self.symbol_table:
            raise Exception(f"At {get_pos_str(simulate)}  "
                            f"{simulate.circuit_id} is not defined before use!")
        for arg in simulate.args:
            arg.accept(self)

    # validate a number
    def visit_num(self, num: Num):
        value = num.value
        if (value is None) or (not value.isdigit()):
            raise Exception(f"At {get_pos_str(num)}  "
                            f"number is invalid!")

    # validate a variable: use of var should be already defined
    def visit_var(self, var: Var):
        if var.identifier not in self.symbol_table:
            raise Exception(f"At {get_pos_str(var)}  "
                            f"{var.identifier} is not defined before use!")

    # validate an output statement
    def visit_output(self, output: Output):
        res = output.res
        res.accept(self)

    # validate a if-then-else
    def visit_ifThenElse(self, if_then_else: IfThenElse):
        cond = if_then_else.cond
        then_stmts = if_then_else.then_statements
        else_stmts = if_then_else.else_statements
        cond.accept(self)

        stmts = then_stmts if not else_stmts else then_stmts + else_stmts
        for stmt in stmts:
            stmt.accept(self)

    # validate a loop
    def visit_loop(self, loop: Loop):
        # put vars defined in loop's inputs into symbol table
        for input_var in loop.inputs:
            if input_var in self.symbol_table:
                raise Exception(f"At {get_pos_str(loop)}  "
                                f"{input_var} is already defined!")
            self.symbol_table[input_var] = None
        for stmt in loop.statements:
            stmt.accept(self)
        # pop out the loop variable since we are leaving the scope of this loop
        for input_var in loop.inputs:
            self.symbol_table.pop(input_var)
