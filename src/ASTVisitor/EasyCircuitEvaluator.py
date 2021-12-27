import copy
import itertools

from schemdraw.parsing import logicparse
from toposort import toposort

from AST.ComponentType import ComponentTypeEnum
from AST.Draw import Draw
from AST.IfThenElse import IfThenElse
from AST.Loop import Loop
from AST.Num import Num
from AST.Output import Output
from AST.Program import Program
from AST.Simulate import Simulate
from AST.Var import Var
from ASTVisitor.BaseASTVisitor import BaseASTVisitor
from ASTVisitor.EasyCircuitDynamicChecker import EasyCircuitDynamicChecker
from src.AST.Circuit import Circuit
from src.AST.Component import Component
from src.AST.Connect import Connect

PLACEHOLDER = "_"


# AST Evaluator: generate program output while visiting.
# Require: AST is already statically validated.
class EasyCircuitEvaluator(BaseASTVisitor):

    def __init__(self):
        self.component_vars_table = {}
        self.circuit_vars_table = {}
        self.loop_vars_table = {}

    def visit_program(self, program: Program):
        for statement in program.statements:
            statement.accept(self)

    def visit_circuit(self, circuit: Circuit):
        # Validate circuit name.
        EasyCircuitDynamicChecker.checkAlreadyDefinedVar(circuit.name, self.circuit_vars_table, circuit)

        for component in circuit.components:
            component.accept(self)

        # Build logic gate structure by using graph and topological sorting.
        # Require: AST is already statically validated.
        graph = {}
        last_input_comp = None
        for connect in circuit.connects:
            [from_comp, to_comp] = connect.accept(self)
            if to_comp.get_type_enum() == ComponentTypeEnum.AND or \
                    to_comp.get_type_enum() == ComponentTypeEnum.OR or \
                    to_comp.get_type_enum() == ComponentTypeEnum.XOR:
                last_input_comp = from_comp
            if from_comp.get_type_enum() == ComponentTypeEnum.CIRCUIT:
                from_comp = copy.deepcopy(from_comp)
            if from_comp not in graph:
                graph[from_comp] = []
            graph[from_comp].append(to_comp)

        logic_gate_structure = list(toposort(graph))    # logic gate structure
        middle_comp = list(logic_gate_structure[1])[0]  # logic component
        bottom_comps = list(logic_gate_structure[2])    # input components

        logic = middle_comp.get_type_enum().name.lower()
        inputs = []
        for comp in bottom_comps:
            if comp.get_type_enum() == ComponentTypeEnum.CIRCUIT:
                inputs.append(self.circuit_vars_table[comp.name])
            else:
                inputs.append(PLACEHOLDER)

        # Stringify logic gate structure.
        if last_input_comp.name == bottom_comps[1].name:
            logic_gate_str = f"( {inputs[0]} {logic} {inputs[1]} )"
        else:
            logic_gate_str = f"( {inputs[1]} {logic} {inputs[0]} )"

        self.component_vars_table[circuit.name] = circuit
        self.circuit_vars_table[circuit.name] = logic_gate_str

    def visit_component(self, component: Component):
        EasyCircuitDynamicChecker.checkAlreadyDefinedVar(component.name, self.component_vars_table, component)
        self.component_vars_table[component.name] = component

    def visit_connect(self, connect: Connect):
        from_name = connect.connect_from
        to_name = connect.connect_to
        # validate the use of name with correct map
        EasyCircuitDynamicChecker.checkUseVarBeforeDefined(from_name,
                                                           {**self.component_vars_table, **self.circuit_vars_table},
                                                           connect)
        EasyCircuitDynamicChecker.checkUseVarBeforeDefined(to_name,
                                                           {**self.component_vars_table, **self.circuit_vars_table},
                                                           connect)

        from_comp = self.component_vars_table[from_name]
        to_comp = self.component_vars_table[to_name]
        return [from_comp, to_comp]

    def visit_draw(self, draw: Draw):
        # Draw circuit with unfilled inputs and output.
        if draw.name is not None:
            EasyCircuitDynamicChecker.checkUseVarBeforeDefined(draw.name, self.circuit_vars_table, draw)

            circuit = self.circuit_vars_table[draw.name]
            counter = 0
            labelled_circuit = ''
            for c in circuit:
                if c == PLACEHOLDER:
                    counter += 1
                    labelled_circuit += 'pos_' + str(counter)
                else:
                    labelled_circuit += c
            logicparse(labelled_circuit, outlabel=draw.name).draw()

        # Draw circuit with filled inputs and output.
        else:
            simulate = draw.simulate
            EasyCircuitDynamicChecker.checkUseVarBeforeDefined(simulate.circuit_id, self.circuit_vars_table, simulate)
            circuit = self.circuit_vars_table[simulate.circuit_id]
            EasyCircuitDynamicChecker.checkParamsArgsNumMismatch(len(simulate.args), circuit.count(PLACEHOLDER),
                                                                 simulate)
            filled_circuit = ''
            i = 0
            for c in circuit:
                if c == PLACEHOLDER:
                    filled_circuit += "input_" + str(simulate.args[i].accept(self))
                    i += 1
                else:
                    filled_circuit += c
            logicparse(filled_circuit, outlabel='output_' + str(simulate.accept(self))).draw()

    def visit_simulate(self, simulate: Simulate):
        EasyCircuitDynamicChecker.checkUseVarBeforeDefined(simulate.circuit_id, self.circuit_vars_table, simulate)
        circuit = self.circuit_vars_table[simulate.circuit_id]
        EasyCircuitDynamicChecker.checkParamsArgsNumMismatch(len(simulate.args), circuit.count(PLACEHOLDER), simulate)

        for arg in simulate.args:
            value = arg.accept(self)
            circuit = circuit.replace(PLACEHOLDER, 'False' if value == 0 else 'True', 1)
        circuit = circuit.replace('xor', '!=')
        return int(eval(circuit))

    def visit_num(self, num: Num):
        return int(num.value)

    def visit_var(self, var: Var):
        EasyCircuitDynamicChecker.checkUseVarBeforeDefined(var.identifier, self.loop_vars_table, var)

        return self.loop_vars_table[var.identifier]

    def visit_output(self, output: Output):
        simulate = output.res
        EasyCircuitDynamicChecker.checkUseVarBeforeDefined(simulate.circuit_id, self.circuit_vars_table, simulate)
        circuit = self.circuit_vars_table[simulate.circuit_id]
        EasyCircuitDynamicChecker.checkParamsArgsNumMismatch(len(simulate.args), circuit.count(PLACEHOLDER), simulate)

        args_to_str = ''
        for arg in simulate.args:
            value = arg.accept(self)
            args_to_str += str(value) + ', '
        args_to_str = args_to_str[:len(args_to_str) - 2]
        print(f"Output: {simulate.circuit_id}({args_to_str}) => {simulate.accept(self)}")

    def visit_ifThenElse(self, if_then_else: IfThenElse):
        value = if_then_else.cond.accept(self)
        if value != 0:
            for statement in if_then_else.then_statements:
                statement.accept(self)
        elif if_then_else.else_statements is not None:
            for statement in if_then_else.else_statements:
                statement.accept(self)

    def visit_loop(self, loop: Loop):
        inputs = loop.inputs
        for input_var in inputs:
            EasyCircuitDynamicChecker.checkAlreadyDefinedVar(input_var, self.loop_vars_table, loop)

        statements = loop.statements
        # cartesian product to get all combinations of input values
        combinations = itertools.product([0, 1], repeat=len(inputs))
        for combination in combinations:
            # Define loop input variables.
            i = 0
            for var in inputs:
                self.loop_vars_table[var] = combination[i]
                i += 1
            # Evaluate loop body.
            for statement in statements:
                statement.accept(self)
            # Undefine loop input variables since they are only accessible in the loop body.
            for var in inputs:
                self.loop_vars_table.pop(var)
