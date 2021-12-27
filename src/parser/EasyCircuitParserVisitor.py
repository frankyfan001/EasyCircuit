# Generated from /Users/chengzhifan/Documents/1 Study/3 UBC/CPSC 410 Advanced Software Engineering/Project1Group3_EasyCircuit/src/grammar/EasyCircuitParser.g4 by ANTLR 4.9.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .EasyCircuitParser import EasyCircuitParser
else:
    from EasyCircuitParser import EasyCircuitParser

# This class defines a complete generic visitor for a parse tree produced by EasyCircuitParser.

class EasyCircuitParserVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by EasyCircuitParser#program.
    def visitProgram(self, ctx:EasyCircuitParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EasyCircuitParser#statement.
    def visitStatement(self, ctx:EasyCircuitParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EasyCircuitParser#circuit.
    def visitCircuit(self, ctx:EasyCircuitParser.CircuitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EasyCircuitParser#component.
    def visitComponent(self, ctx:EasyCircuitParser.ComponentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EasyCircuitParser#connect.
    def visitConnect(self, ctx:EasyCircuitParser.ConnectContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EasyCircuitParser#draw.
    def visitDraw(self, ctx:EasyCircuitParser.DrawContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EasyCircuitParser#simulate.
    def visitSimulate(self, ctx:EasyCircuitParser.SimulateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EasyCircuitParser#args.
    def visitArgs(self, ctx:EasyCircuitParser.ArgsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EasyCircuitParser#exp.
    def visitExp(self, ctx:EasyCircuitParser.ExpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EasyCircuitParser#num.
    def visitNum(self, ctx:EasyCircuitParser.NumContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EasyCircuitParser#var.
    def visitVar(self, ctx:EasyCircuitParser.VarContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EasyCircuitParser#output.
    def visitOutput(self, ctx:EasyCircuitParser.OutputContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EasyCircuitParser#ifthenelse.
    def visitIfthenelse(self, ctx:EasyCircuitParser.IfthenelseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EasyCircuitParser#statements.
    def visitStatements(self, ctx:EasyCircuitParser.StatementsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EasyCircuitParser#loop.
    def visitLoop(self, ctx:EasyCircuitParser.LoopContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EasyCircuitParser#inputs.
    def visitInputs(self, ctx:EasyCircuitParser.InputsContext):
        return self.visitChildren(ctx)



del EasyCircuitParser