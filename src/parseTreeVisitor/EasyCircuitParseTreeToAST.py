from AST.IfThenElse import IfThenElse
from AST.Loop import Loop
from AST.Num import Num
from AST.Output import Output
from AST.Simulate import Simulate
from AST.Var import Var
from src.AST.Circuit import Circuit
from src.AST.Component import Component
from src.AST.ComponentType import ComponentType
from src.AST.Connect import Connect
from src.AST.Draw import Draw
from src.AST.Program import Program
from src.common.common import TYPECHECK_MAP
from src.parser.EasyCircuitParser import EasyCircuitParser
from src.parser.EasyCircuitParserVisitor import EasyCircuitParserVisitor


# This class completely visit a parse tree and produce an abstract syntax tree (AST).
class EasyCircuitParseTreeVisitor(EasyCircuitParserVisitor):

    # Visit a parse tree produced by EasyCircuitParser#program.
    def visitProgram(self, ctx: EasyCircuitParser.ProgramContext) -> Program:
        statements = []
        for s in ctx.statement():
            statements.append(self.visitStatement(s))
        return Program(statements)

    # Visit a parse tree produced by EasyCircuitParser#statement.
    def visitStatement(self, ctx: EasyCircuitParser.StatementContext):
        if ctx.circuit() is not None:
            return self.visitCircuit(ctx.circuit())
        elif ctx.component() is not None:
            return self.visitComponent(ctx.component())
        elif ctx.connect() is not None:
            return self.visitConnect(ctx.connect())
        elif ctx.draw() is not None:
            return self.visitDraw(ctx.draw())
        elif ctx.simulate() is not None:
            return self.visitSimulate(ctx.simulate())
        elif ctx.output() is not None:
            return self.visitOutput(ctx.output())
        elif ctx.ifthenelse() is not None:
            return self.visitIfthenelse(ctx.ifthenelse())
        elif ctx.loop() is not None:
            return self.visitLoop(ctx.loop())
        else:
            raise Exception("Statement parse tree with invalid context information.")

    # Visit a parse tree produced by EasyCircuitParser#circuit.
    def visitCircuit(self, ctx: EasyCircuitParser.CircuitContext) -> Circuit:
        name = ctx.ID().getText()

        component_type_enum, comp_input, comp_output = TYPECHECK_MAP[ctx.CIRCUIT_START().getText()]
        comp_type = ComponentType(component_type_enum, comp_input, comp_output)

        components = []
        for component in ctx.component():
            components.append(self.visitComponent(component))
        connects = []
        for connect in ctx.connect():
            connects.append(self.visitConnect(connect))

        return Circuit(name, comp_type, components, connects, ctx.start)

    # Visit a parse tree produced by EasyCircuitParser#component.
    def visitComponent(self, ctx: EasyCircuitParser.ComponentContext) -> Component:
        if ctx.TYPE() is not None:
            name = ctx.ID().getText()
            component_type_enum, comp_input, comp_output = TYPECHECK_MAP[ctx.TYPE().getText()]
            comp_type = ComponentType(component_type_enum, comp_input, comp_output)
            return Component(name, comp_type, ctx.start)
        elif ctx.circuit() is not None:
            return self.visitCircuit(ctx.circuit())
        else:
            raise Exception("Component parse tree with invalid context information.")

    # Visit a parse tree produced by EasyCircuitParser#connect.
    def visitConnect(self, ctx: EasyCircuitParser.ConnectContext) -> Connect:
        connect_from = ctx.ID(0).getText()
        connect_to = ctx.ID(1).getText()
        return Connect(connect_from, connect_to, ctx.start)

    # Visit a parse tree produced by EasyCircuitParser#draw.
    def visitDraw(self, ctx: EasyCircuitParser.DrawContext) -> Draw:
        if ctx.ID() is not None:
            return Draw(ctx.ID().getText(), None, ctx.start)
        elif ctx.simulate() is not None:
            return Draw(None, self.visitSimulate(ctx.simulate()), ctx.start)
        else:
            raise Exception("Draw parse tree with invalid context information.")

    # Visit a parse tree produced by EasyCircuitParser#simulate.
    def visitSimulate(self, ctx: EasyCircuitParser.SimulateContext) -> Simulate:
        circuit_id = ctx.ID().getText()
        args = self.visitArgs(ctx.args())
        return Simulate(circuit_id, args, ctx.start)

    # Visit a parse tree produced by EasyCircuitParser#args.
    def visitArgs(self, ctx: EasyCircuitParser.ArgsContext):
        args = []
        for exp in ctx.exp():
            args.append(self.visitExp(exp))
        return args

    # Visit a parse tree produced by EasyCircuitParser#exp.
    def visitExp(self, ctx: EasyCircuitParser.ExpContext):
        if ctx.num():
            return self.visitNum(ctx.num())
        elif ctx.var():
            return self.visitVar(ctx.var())
        elif ctx.simulate():
            return self.visitSimulate(ctx.simulate())
        else:
            raise Exception("Exp parse tree with invalid context information.")

    # Visit a parse tree produced by EasyCircuitParser#num.
    def visitNum(self, ctx: EasyCircuitParser.NumContext) -> Num:
        return Num(ctx.NUM().getText(), ctx.start)

    # Visit a parse tree produced by EasyCircuitParser#var.
    def visitVar(self, ctx: EasyCircuitParser.VarContext) -> Var:
        return Var(ctx.ID().getText(), ctx.start)

    # Visit a parse tree produced by EasyCircuitParser#output.
    def visitOutput(self, ctx: EasyCircuitParser.OutputContext) -> Output:
        return Output(self.visitSimulate(ctx.simulate()), ctx.start)

    # Visit a parse tree produced by EasyCircuitParser#ifthenelse.
    def visitIfthenelse(self, ctx: EasyCircuitParser.IfthenelseContext) -> IfThenElse:
        cond = self.visitExp(ctx.exp())

        then_statements = []
        for s in ctx.thenblock.statement():
            then_statements.append(self.visitStatement(s))

        else_statements = []
        if ctx.elseblock is None:
            else_statements = None
        else:
            for s in ctx.elseblock.statement():
                else_statements.append(self.visitStatement(s))

        return IfThenElse(cond, then_statements, else_statements, ctx.start)

    # Visit a parse tree produced by EasyCircuitParser#statements.
    def visitStatements(self, ctx: EasyCircuitParser.StatementsContext):
        statements = []
        for s in ctx.statement():
            self.visitStatement(s)
        return statements

    # Visit a parse tree produced by EasyCircuitParser#loop.
    def visitLoop(self, ctx: EasyCircuitParser.LoopContext) -> Loop:
        inputs = self.visitInputs(ctx.inputs())
        statements = []
        for s in ctx.statement():
            statements.append(self.visitStatement(s))
        return Loop(inputs, statements, ctx.start)

    # Visit a parse tree produced by EasyCircuitParser#inputs.
    def visitInputs(self, ctx: EasyCircuitParser.InputsContext):
        inputs = []
        for i in ctx.ID():
            inputs.append(i.getText())
        return inputs
