# Generated from /Users/chengzhifan/Documents/1 Study/3 UBC/CPSC 410 Advanced Software Engineering/Project1Group3_EasyCircuit/src/grammar/EasyCircuitParser.g4 by ANTLR 4.9.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\26")
        buf.write("\u009b\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\3\2\7\2$\n\2\f\2\16")
        buf.write("\2\'\13\2\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\5\3\61\n\3\3")
        buf.write("\4\3\4\3\4\3\4\7\4\67\n\4\f\4\16\4:\13\4\3\4\6\4=\n\4")
        buf.write("\r\4\16\4>\3\4\3\4\3\5\3\5\3\5\3\5\5\5G\n\5\3\6\3\6\3")
        buf.write("\6\3\6\3\6\3\7\3\7\3\7\5\7Q\n\7\3\7\3\7\3\b\3\b\3\b\3")
        buf.write("\b\3\b\5\bZ\n\b\3\t\3\t\3\t\7\t_\n\t\f\t\16\tb\13\t\3")
        buf.write("\t\3\t\3\n\3\n\3\n\5\ni\n\n\3\13\3\13\3\f\3\f\3\r\3\r")
        buf.write("\3\r\3\r\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16")
        buf.write("\3\16\5\16}\n\16\3\17\7\17\u0080\n\17\f\17\16\17\u0083")
        buf.write("\13\17\3\20\3\20\3\20\3\20\3\20\3\20\7\20\u008b\n\20\f")
        buf.write("\20\16\20\u008e\13\20\3\20\3\20\3\21\3\21\7\21\u0094\n")
        buf.write("\21\f\21\16\21\u0097\13\21\3\21\3\21\3\21\2\2\22\2\4\6")
        buf.write("\b\n\f\16\20\22\24\26\30\32\34\36 \2\2\2\u009e\2%\3\2")
        buf.write("\2\2\4\60\3\2\2\2\6\62\3\2\2\2\bF\3\2\2\2\nH\3\2\2\2\f")
        buf.write("M\3\2\2\2\16T\3\2\2\2\20`\3\2\2\2\22h\3\2\2\2\24j\3\2")
        buf.write("\2\2\26l\3\2\2\2\30n\3\2\2\2\32r\3\2\2\2\34\u0081\3\2")
        buf.write("\2\2\36\u0084\3\2\2\2 \u0095\3\2\2\2\"$\5\4\3\2#\"\3\2")
        buf.write("\2\2$\'\3\2\2\2%#\3\2\2\2%&\3\2\2\2&\3\3\2\2\2\'%\3\2")
        buf.write("\2\2(\61\5\6\4\2)\61\5\b\5\2*\61\5\n\6\2+\61\5\f\7\2,")
        buf.write("\61\5\16\b\2-\61\5\30\r\2.\61\5\32\16\2/\61\5\36\20\2")
        buf.write("\60(\3\2\2\2\60)\3\2\2\2\60*\3\2\2\2\60+\3\2\2\2\60,\3")
        buf.write("\2\2\2\60-\3\2\2\2\60.\3\2\2\2\60/\3\2\2\2\61\5\3\2\2")
        buf.write("\2\62\63\7\3\2\2\63\64\7\25\2\2\648\7\4\2\2\65\67\5\b")
        buf.write("\5\2\66\65\3\2\2\2\67:\3\2\2\28\66\3\2\2\289\3\2\2\29")
        buf.write("<\3\2\2\2:8\3\2\2\2;=\5\n\6\2<;\3\2\2\2=>\3\2\2\2><\3")
        buf.write("\2\2\2>?\3\2\2\2?@\3\2\2\2@A\7\5\2\2A\7\3\2\2\2BC\7\16")
        buf.write("\2\2CD\7\25\2\2DG\7\n\2\2EG\5\6\4\2FB\3\2\2\2FE\3\2\2")
        buf.write("\2G\t\3\2\2\2HI\7\25\2\2IJ\7\13\2\2JK\7\25\2\2KL\7\n\2")
        buf.write("\2L\13\3\2\2\2MP\7\17\2\2NQ\7\25\2\2OQ\5\16\b\2PN\3\2")
        buf.write("\2\2PO\3\2\2\2QR\3\2\2\2RS\7\n\2\2S\r\3\2\2\2TU\7\25\2")
        buf.write("\2UV\7\6\2\2VW\5\20\t\2WY\7\7\2\2XZ\7\n\2\2YX\3\2\2\2")
        buf.write("YZ\3\2\2\2Z\17\3\2\2\2[\\\5\22\n\2\\]\7\f\2\2]_\3\2\2")
        buf.write("\2^[\3\2\2\2_b\3\2\2\2`^\3\2\2\2`a\3\2\2\2ac\3\2\2\2b")
        buf.write("`\3\2\2\2cd\5\22\n\2d\21\3\2\2\2ei\5\24\13\2fi\5\26\f")
        buf.write("\2gi\5\16\b\2he\3\2\2\2hf\3\2\2\2hg\3\2\2\2i\23\3\2\2")
        buf.write("\2jk\7\24\2\2k\25\3\2\2\2lm\7\25\2\2m\27\3\2\2\2no\7\20")
        buf.write("\2\2op\5\16\b\2pq\7\n\2\2q\31\3\2\2\2rs\7\21\2\2st\5\22")
        buf.write("\n\2tu\7\4\2\2uv\5\34\17\2v|\7\5\2\2wx\7\22\2\2xy\7\4")
        buf.write("\2\2yz\5\34\17\2z{\7\5\2\2{}\3\2\2\2|w\3\2\2\2|}\3\2\2")
        buf.write("\2}\33\3\2\2\2~\u0080\5\4\3\2\177~\3\2\2\2\u0080\u0083")
        buf.write("\3\2\2\2\u0081\177\3\2\2\2\u0081\u0082\3\2\2\2\u0082\35")
        buf.write("\3\2\2\2\u0083\u0081\3\2\2\2\u0084\u0085\7\23\2\2\u0085")
        buf.write("\u0086\7\b\2\2\u0086\u0087\5 \21\2\u0087\u0088\7\t\2\2")
        buf.write("\u0088\u008c\7\4\2\2\u0089\u008b\5\4\3\2\u008a\u0089\3")
        buf.write("\2\2\2\u008b\u008e\3\2\2\2\u008c\u008a\3\2\2\2\u008c\u008d")
        buf.write("\3\2\2\2\u008d\u008f\3\2\2\2\u008e\u008c\3\2\2\2\u008f")
        buf.write("\u0090\7\5\2\2\u0090\37\3\2\2\2\u0091\u0092\7\25\2\2\u0092")
        buf.write("\u0094\7\f\2\2\u0093\u0091\3\2\2\2\u0094\u0097\3\2\2\2")
        buf.write("\u0095\u0093\3\2\2\2\u0095\u0096\3\2\2\2\u0096\u0098\3")
        buf.write("\2\2\2\u0097\u0095\3\2\2\2\u0098\u0099\7\25\2\2\u0099")
        buf.write("!\3\2\2\2\17%\608>FPY`h|\u0081\u008c\u0095")
        return buf.getvalue()


class EasyCircuitParser ( Parser ):

    grammarFileName = "EasyCircuitParser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'CIRCUIT '", "'{'", "'}'", "'('", "')'", 
                     "'['", "']'", "';'", "<INVALID>", "','", "'='", "<INVALID>", 
                     "'draw '", "'output '", "'if '", "'else'", "'loop '" ]

    symbolicNames = [ "<INVALID>", "CIRCUIT_START", "LEFT_BRACKET", "RIGHT_BRACKET", 
                      "LEFT_PAREN", "RIGHT_PAREN", "LEFT_SQUARE_BRACKET", 
                      "RIGHT_SQUARE_BRACKET", "SEMICOLON", "ARROW", "COMMA", 
                      "EQ", "TYPE", "DRAW_START", "OUTPUT_START", "IF", 
                      "ELSE", "LOOP_START", "NUM", "ID", "WS" ]

    RULE_program = 0
    RULE_statement = 1
    RULE_circuit = 2
    RULE_component = 3
    RULE_connect = 4
    RULE_draw = 5
    RULE_simulate = 6
    RULE_args = 7
    RULE_exp = 8
    RULE_num = 9
    RULE_var = 10
    RULE_output = 11
    RULE_ifthenelse = 12
    RULE_statements = 13
    RULE_loop = 14
    RULE_inputs = 15

    ruleNames =  [ "program", "statement", "circuit", "component", "connect", 
                   "draw", "simulate", "args", "exp", "num", "var", "output", 
                   "ifthenelse", "statements", "loop", "inputs" ]

    EOF = Token.EOF
    CIRCUIT_START=1
    LEFT_BRACKET=2
    RIGHT_BRACKET=3
    LEFT_PAREN=4
    RIGHT_PAREN=5
    LEFT_SQUARE_BRACKET=6
    RIGHT_SQUARE_BRACKET=7
    SEMICOLON=8
    ARROW=9
    COMMA=10
    EQ=11
    TYPE=12
    DRAW_START=13
    OUTPUT_START=14
    IF=15
    ELSE=16
    LOOP_START=17
    NUM=18
    ID=19
    WS=20

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(EasyCircuitParser.StatementContext)
            else:
                return self.getTypedRuleContext(EasyCircuitParser.StatementContext,i)


        def getRuleIndex(self):
            return EasyCircuitParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = EasyCircuitParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 35
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << EasyCircuitParser.CIRCUIT_START) | (1 << EasyCircuitParser.TYPE) | (1 << EasyCircuitParser.DRAW_START) | (1 << EasyCircuitParser.OUTPUT_START) | (1 << EasyCircuitParser.IF) | (1 << EasyCircuitParser.LOOP_START) | (1 << EasyCircuitParser.ID))) != 0):
                self.state = 32
                self.statement()
                self.state = 37
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def circuit(self):
            return self.getTypedRuleContext(EasyCircuitParser.CircuitContext,0)


        def component(self):
            return self.getTypedRuleContext(EasyCircuitParser.ComponentContext,0)


        def connect(self):
            return self.getTypedRuleContext(EasyCircuitParser.ConnectContext,0)


        def draw(self):
            return self.getTypedRuleContext(EasyCircuitParser.DrawContext,0)


        def simulate(self):
            return self.getTypedRuleContext(EasyCircuitParser.SimulateContext,0)


        def output(self):
            return self.getTypedRuleContext(EasyCircuitParser.OutputContext,0)


        def ifthenelse(self):
            return self.getTypedRuleContext(EasyCircuitParser.IfthenelseContext,0)


        def loop(self):
            return self.getTypedRuleContext(EasyCircuitParser.LoopContext,0)


        def getRuleIndex(self):
            return EasyCircuitParser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = EasyCircuitParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_statement)
        try:
            self.state = 46
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 38
                self.circuit()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 39
                self.component()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 40
                self.connect()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 41
                self.draw()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 42
                self.simulate()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 43
                self.output()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 44
                self.ifthenelse()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 45
                self.loop()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CircuitContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CIRCUIT_START(self):
            return self.getToken(EasyCircuitParser.CIRCUIT_START, 0)

        def ID(self):
            return self.getToken(EasyCircuitParser.ID, 0)

        def LEFT_BRACKET(self):
            return self.getToken(EasyCircuitParser.LEFT_BRACKET, 0)

        def RIGHT_BRACKET(self):
            return self.getToken(EasyCircuitParser.RIGHT_BRACKET, 0)

        def component(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(EasyCircuitParser.ComponentContext)
            else:
                return self.getTypedRuleContext(EasyCircuitParser.ComponentContext,i)


        def connect(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(EasyCircuitParser.ConnectContext)
            else:
                return self.getTypedRuleContext(EasyCircuitParser.ConnectContext,i)


        def getRuleIndex(self):
            return EasyCircuitParser.RULE_circuit

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCircuit" ):
                listener.enterCircuit(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCircuit" ):
                listener.exitCircuit(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCircuit" ):
                return visitor.visitCircuit(self)
            else:
                return visitor.visitChildren(self)




    def circuit(self):

        localctx = EasyCircuitParser.CircuitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_circuit)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 48
            self.match(EasyCircuitParser.CIRCUIT_START)
            self.state = 49
            self.match(EasyCircuitParser.ID)
            self.state = 50
            self.match(EasyCircuitParser.LEFT_BRACKET)
            self.state = 54
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==EasyCircuitParser.CIRCUIT_START or _la==EasyCircuitParser.TYPE:
                self.state = 51
                self.component()
                self.state = 56
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 58 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 57
                self.connect()
                self.state = 60 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==EasyCircuitParser.ID):
                    break

            self.state = 62
            self.match(EasyCircuitParser.RIGHT_BRACKET)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ComponentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TYPE(self):
            return self.getToken(EasyCircuitParser.TYPE, 0)

        def ID(self):
            return self.getToken(EasyCircuitParser.ID, 0)

        def SEMICOLON(self):
            return self.getToken(EasyCircuitParser.SEMICOLON, 0)

        def circuit(self):
            return self.getTypedRuleContext(EasyCircuitParser.CircuitContext,0)


        def getRuleIndex(self):
            return EasyCircuitParser.RULE_component

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComponent" ):
                listener.enterComponent(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComponent" ):
                listener.exitComponent(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitComponent" ):
                return visitor.visitComponent(self)
            else:
                return visitor.visitChildren(self)




    def component(self):

        localctx = EasyCircuitParser.ComponentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_component)
        try:
            self.state = 68
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [EasyCircuitParser.TYPE]:
                self.enterOuterAlt(localctx, 1)
                self.state = 64
                self.match(EasyCircuitParser.TYPE)
                self.state = 65
                self.match(EasyCircuitParser.ID)
                self.state = 66
                self.match(EasyCircuitParser.SEMICOLON)
                pass
            elif token in [EasyCircuitParser.CIRCUIT_START]:
                self.enterOuterAlt(localctx, 2)
                self.state = 67
                self.circuit()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConnectContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(EasyCircuitParser.ID)
            else:
                return self.getToken(EasyCircuitParser.ID, i)

        def ARROW(self):
            return self.getToken(EasyCircuitParser.ARROW, 0)

        def SEMICOLON(self):
            return self.getToken(EasyCircuitParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return EasyCircuitParser.RULE_connect

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConnect" ):
                listener.enterConnect(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConnect" ):
                listener.exitConnect(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConnect" ):
                return visitor.visitConnect(self)
            else:
                return visitor.visitChildren(self)




    def connect(self):

        localctx = EasyCircuitParser.ConnectContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_connect)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 70
            self.match(EasyCircuitParser.ID)
            self.state = 71
            self.match(EasyCircuitParser.ARROW)
            self.state = 72
            self.match(EasyCircuitParser.ID)
            self.state = 73
            self.match(EasyCircuitParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DrawContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DRAW_START(self):
            return self.getToken(EasyCircuitParser.DRAW_START, 0)

        def SEMICOLON(self):
            return self.getToken(EasyCircuitParser.SEMICOLON, 0)

        def ID(self):
            return self.getToken(EasyCircuitParser.ID, 0)

        def simulate(self):
            return self.getTypedRuleContext(EasyCircuitParser.SimulateContext,0)


        def getRuleIndex(self):
            return EasyCircuitParser.RULE_draw

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDraw" ):
                listener.enterDraw(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDraw" ):
                listener.exitDraw(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDraw" ):
                return visitor.visitDraw(self)
            else:
                return visitor.visitChildren(self)




    def draw(self):

        localctx = EasyCircuitParser.DrawContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_draw)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 75
            self.match(EasyCircuitParser.DRAW_START)
            self.state = 78
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.state = 76
                self.match(EasyCircuitParser.ID)
                pass

            elif la_ == 2:
                self.state = 77
                self.simulate()
                pass


            self.state = 80
            self.match(EasyCircuitParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SimulateContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(EasyCircuitParser.ID, 0)

        def LEFT_PAREN(self):
            return self.getToken(EasyCircuitParser.LEFT_PAREN, 0)

        def args(self):
            return self.getTypedRuleContext(EasyCircuitParser.ArgsContext,0)


        def RIGHT_PAREN(self):
            return self.getToken(EasyCircuitParser.RIGHT_PAREN, 0)

        def SEMICOLON(self):
            return self.getToken(EasyCircuitParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return EasyCircuitParser.RULE_simulate

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSimulate" ):
                listener.enterSimulate(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSimulate" ):
                listener.exitSimulate(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSimulate" ):
                return visitor.visitSimulate(self)
            else:
                return visitor.visitChildren(self)




    def simulate(self):

        localctx = EasyCircuitParser.SimulateContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_simulate)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 82
            self.match(EasyCircuitParser.ID)
            self.state = 83
            self.match(EasyCircuitParser.LEFT_PAREN)
            self.state = 84
            self.args()
            self.state = 85
            self.match(EasyCircuitParser.RIGHT_PAREN)
            self.state = 87
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.state = 86
                self.match(EasyCircuitParser.SEMICOLON)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArgsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(EasyCircuitParser.ExpContext)
            else:
                return self.getTypedRuleContext(EasyCircuitParser.ExpContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(EasyCircuitParser.COMMA)
            else:
                return self.getToken(EasyCircuitParser.COMMA, i)

        def getRuleIndex(self):
            return EasyCircuitParser.RULE_args

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArgs" ):
                listener.enterArgs(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArgs" ):
                listener.exitArgs(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArgs" ):
                return visitor.visitArgs(self)
            else:
                return visitor.visitChildren(self)




    def args(self):

        localctx = EasyCircuitParser.ArgsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_args)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 94
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,7,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 89
                    self.exp()
                    self.state = 90
                    self.match(EasyCircuitParser.COMMA) 
                self.state = 96
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,7,self._ctx)

            self.state = 97
            self.exp()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def num(self):
            return self.getTypedRuleContext(EasyCircuitParser.NumContext,0)


        def var(self):
            return self.getTypedRuleContext(EasyCircuitParser.VarContext,0)


        def simulate(self):
            return self.getTypedRuleContext(EasyCircuitParser.SimulateContext,0)


        def getRuleIndex(self):
            return EasyCircuitParser.RULE_exp

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExp" ):
                listener.enterExp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExp" ):
                listener.exitExp(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp" ):
                return visitor.visitExp(self)
            else:
                return visitor.visitChildren(self)




    def exp(self):

        localctx = EasyCircuitParser.ExpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_exp)
        try:
            self.state = 102
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 99
                self.num()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 100
                self.var()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 101
                self.simulate()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NumContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUM(self):
            return self.getToken(EasyCircuitParser.NUM, 0)

        def getRuleIndex(self):
            return EasyCircuitParser.RULE_num

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNum" ):
                listener.enterNum(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNum" ):
                listener.exitNum(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNum" ):
                return visitor.visitNum(self)
            else:
                return visitor.visitChildren(self)




    def num(self):

        localctx = EasyCircuitParser.NumContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_num)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 104
            self.match(EasyCircuitParser.NUM)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VarContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(EasyCircuitParser.ID, 0)

        def getRuleIndex(self):
            return EasyCircuitParser.RULE_var

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVar" ):
                listener.enterVar(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVar" ):
                listener.exitVar(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar" ):
                return visitor.visitVar(self)
            else:
                return visitor.visitChildren(self)




    def var(self):

        localctx = EasyCircuitParser.VarContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_var)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 106
            self.match(EasyCircuitParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OutputContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OUTPUT_START(self):
            return self.getToken(EasyCircuitParser.OUTPUT_START, 0)

        def simulate(self):
            return self.getTypedRuleContext(EasyCircuitParser.SimulateContext,0)


        def SEMICOLON(self):
            return self.getToken(EasyCircuitParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return EasyCircuitParser.RULE_output

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOutput" ):
                listener.enterOutput(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOutput" ):
                listener.exitOutput(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOutput" ):
                return visitor.visitOutput(self)
            else:
                return visitor.visitChildren(self)




    def output(self):

        localctx = EasyCircuitParser.OutputContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_output)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 108
            self.match(EasyCircuitParser.OUTPUT_START)
            self.state = 109
            self.simulate()
            self.state = 110
            self.match(EasyCircuitParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IfthenelseContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.thenblock = None # StatementsContext
            self.elseblock = None # StatementsContext

        def IF(self):
            return self.getToken(EasyCircuitParser.IF, 0)

        def exp(self):
            return self.getTypedRuleContext(EasyCircuitParser.ExpContext,0)


        def LEFT_BRACKET(self, i:int=None):
            if i is None:
                return self.getTokens(EasyCircuitParser.LEFT_BRACKET)
            else:
                return self.getToken(EasyCircuitParser.LEFT_BRACKET, i)

        def RIGHT_BRACKET(self, i:int=None):
            if i is None:
                return self.getTokens(EasyCircuitParser.RIGHT_BRACKET)
            else:
                return self.getToken(EasyCircuitParser.RIGHT_BRACKET, i)

        def statements(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(EasyCircuitParser.StatementsContext)
            else:
                return self.getTypedRuleContext(EasyCircuitParser.StatementsContext,i)


        def ELSE(self):
            return self.getToken(EasyCircuitParser.ELSE, 0)

        def getRuleIndex(self):
            return EasyCircuitParser.RULE_ifthenelse

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIfthenelse" ):
                listener.enterIfthenelse(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIfthenelse" ):
                listener.exitIfthenelse(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfthenelse" ):
                return visitor.visitIfthenelse(self)
            else:
                return visitor.visitChildren(self)




    def ifthenelse(self):

        localctx = EasyCircuitParser.IfthenelseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_ifthenelse)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 112
            self.match(EasyCircuitParser.IF)
            self.state = 113
            self.exp()
            self.state = 114
            self.match(EasyCircuitParser.LEFT_BRACKET)
            self.state = 115
            localctx.thenblock = self.statements()
            self.state = 116
            self.match(EasyCircuitParser.RIGHT_BRACKET)
            self.state = 122
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==EasyCircuitParser.ELSE:
                self.state = 117
                self.match(EasyCircuitParser.ELSE)
                self.state = 118
                self.match(EasyCircuitParser.LEFT_BRACKET)
                self.state = 119
                localctx.elseblock = self.statements()
                self.state = 120
                self.match(EasyCircuitParser.RIGHT_BRACKET)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(EasyCircuitParser.StatementContext)
            else:
                return self.getTypedRuleContext(EasyCircuitParser.StatementContext,i)


        def getRuleIndex(self):
            return EasyCircuitParser.RULE_statements

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatements" ):
                listener.enterStatements(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatements" ):
                listener.exitStatements(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatements" ):
                return visitor.visitStatements(self)
            else:
                return visitor.visitChildren(self)




    def statements(self):

        localctx = EasyCircuitParser.StatementsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_statements)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 127
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << EasyCircuitParser.CIRCUIT_START) | (1 << EasyCircuitParser.TYPE) | (1 << EasyCircuitParser.DRAW_START) | (1 << EasyCircuitParser.OUTPUT_START) | (1 << EasyCircuitParser.IF) | (1 << EasyCircuitParser.LOOP_START) | (1 << EasyCircuitParser.ID))) != 0):
                self.state = 124
                self.statement()
                self.state = 129
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LoopContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LOOP_START(self):
            return self.getToken(EasyCircuitParser.LOOP_START, 0)

        def LEFT_SQUARE_BRACKET(self):
            return self.getToken(EasyCircuitParser.LEFT_SQUARE_BRACKET, 0)

        def inputs(self):
            return self.getTypedRuleContext(EasyCircuitParser.InputsContext,0)


        def RIGHT_SQUARE_BRACKET(self):
            return self.getToken(EasyCircuitParser.RIGHT_SQUARE_BRACKET, 0)

        def LEFT_BRACKET(self):
            return self.getToken(EasyCircuitParser.LEFT_BRACKET, 0)

        def RIGHT_BRACKET(self):
            return self.getToken(EasyCircuitParser.RIGHT_BRACKET, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(EasyCircuitParser.StatementContext)
            else:
                return self.getTypedRuleContext(EasyCircuitParser.StatementContext,i)


        def getRuleIndex(self):
            return EasyCircuitParser.RULE_loop

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLoop" ):
                listener.enterLoop(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLoop" ):
                listener.exitLoop(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLoop" ):
                return visitor.visitLoop(self)
            else:
                return visitor.visitChildren(self)




    def loop(self):

        localctx = EasyCircuitParser.LoopContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_loop)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 130
            self.match(EasyCircuitParser.LOOP_START)
            self.state = 131
            self.match(EasyCircuitParser.LEFT_SQUARE_BRACKET)
            self.state = 132
            self.inputs()
            self.state = 133
            self.match(EasyCircuitParser.RIGHT_SQUARE_BRACKET)
            self.state = 134
            self.match(EasyCircuitParser.LEFT_BRACKET)
            self.state = 138
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << EasyCircuitParser.CIRCUIT_START) | (1 << EasyCircuitParser.TYPE) | (1 << EasyCircuitParser.DRAW_START) | (1 << EasyCircuitParser.OUTPUT_START) | (1 << EasyCircuitParser.IF) | (1 << EasyCircuitParser.LOOP_START) | (1 << EasyCircuitParser.ID))) != 0):
                self.state = 135
                self.statement()
                self.state = 140
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 141
            self.match(EasyCircuitParser.RIGHT_BRACKET)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InputsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(EasyCircuitParser.ID)
            else:
                return self.getToken(EasyCircuitParser.ID, i)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(EasyCircuitParser.COMMA)
            else:
                return self.getToken(EasyCircuitParser.COMMA, i)

        def getRuleIndex(self):
            return EasyCircuitParser.RULE_inputs

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInputs" ):
                listener.enterInputs(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInputs" ):
                listener.exitInputs(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInputs" ):
                return visitor.visitInputs(self)
            else:
                return visitor.visitChildren(self)




    def inputs(self):

        localctx = EasyCircuitParser.InputsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_inputs)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 147
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,12,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 143
                    self.match(EasyCircuitParser.ID)
                    self.state = 144
                    self.match(EasyCircuitParser.COMMA) 
                self.state = 149
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,12,self._ctx)

            self.state = 150
            self.match(EasyCircuitParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





