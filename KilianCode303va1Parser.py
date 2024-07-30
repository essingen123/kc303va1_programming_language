# Generated from KilianCode303va1.g4 by ANTLR 4.7.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys

def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\30")
        buf.write("Q\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\4\t\t\t\4\n\t\n\3\2\7\2\26\n\2\f\2\16\2\31\13\2\3")
        buf.write("\2\3\2\3\3\3\3\3\3\7\3 \n\3\f\3\16\3#\13\3\3\4\3\4\3\4")
        buf.write("\3\4\3\4\5\4*\n\4\3\5\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6")
        buf.write("\5\6\65\n\6\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\5")
        buf.write("\7A\n\7\3\b\3\b\3\b\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3")
        buf.write("\n\5\nO\n\n\3\n\2\2\13\2\4\6\b\n\f\16\20\22\2\3\3\2\f")
        buf.write("\22\2R\2\27\3\2\2\2\4\34\3\2\2\2\6)\3\2\2\2\b+\3\2\2\2")
        buf.write("\n/\3\2\2\2\f@\3\2\2\2\16B\3\2\2\2\20E\3\2\2\2\22N\3\2")
        buf.write("\2\2\24\26\5\4\3\2\25\24\3\2\2\2\26\31\3\2\2\2\27\25\3")
        buf.write("\2\2\2\27\30\3\2\2\2\30\32\3\2\2\2\31\27\3\2\2\2\32\33")
        buf.write("\7\2\2\3\33\3\3\2\2\2\34\35\7\3\2\2\35!\7\23\2\2\36 \5")
        buf.write("\6\4\2\37\36\3\2\2\2 #\3\2\2\2!\37\3\2\2\2!\"\3\2\2\2")
        buf.write("\"\5\3\2\2\2#!\3\2\2\2$*\5\b\5\2%*\5\n\6\2&*\5\f\7\2\'")
        buf.write("*\5\16\b\2(*\5\20\t\2)$\3\2\2\2)%\3\2\2\2)&\3\2\2\2)\'")
        buf.write("\3\2\2\2)(\3\2\2\2*\7\3\2\2\2+,\7\23\2\2,-\7\4\2\2-.\5")
        buf.write("\22\n\2.\t\3\2\2\2/\60\7\5\2\2\60\61\5\22\n\2\61\64\5")
        buf.write("\6\4\2\62\63\7\6\2\2\63\65\5\6\4\2\64\62\3\2\2\2\64\65")
        buf.write("\3\2\2\2\65\13\3\2\2\2\66\67\7\7\2\2\678\5\22\n\289\5")
        buf.write("\6\4\29A\3\2\2\2:;\7\b\2\2;<\7\23\2\2<=\7\t\2\2=>\5\22")
        buf.write("\n\2>?\5\6\4\2?A\3\2\2\2@\66\3\2\2\2@:\3\2\2\2A\r\3\2")
        buf.write("\2\2BC\7\n\2\2CD\7\23\2\2D\17\3\2\2\2EF\7\13\2\2FG\5\22")
        buf.write("\n\2G\21\3\2\2\2HI\7\23\2\2IJ\t\2\2\2JO\7\23\2\2KO\7\23")
        buf.write("\2\2LO\7\25\2\2MO\7\26\2\2NH\3\2\2\2NK\3\2\2\2NL\3\2\2")
        buf.write("\2NM\3\2\2\2O\23\3\2\2\2\b\27!)\64@N")
        return buf.getvalue()


class KilianCode303va1Parser ( Parser ):

    grammarFileName = "KilianCode303va1.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'\u00A7\u00A7f\u00A7'", "'='", "'if'", 
                     "'else'", "'while'", "'for'", "'in'", "'\u00A7f\u00A7'", 
                     "'return'", "'+'", "'-'", "'*'", "'/'", "'%'", "'\u00A7lo\u00A7'", 
                     "'=='" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "IDENTIFIER", "NAME", "STRING", "NUMBER", 
                      "COMMENT", "WS" ]

    RULE_program = 0
    RULE_functionDefinition = 1
    RULE_statement = 2
    RULE_assignment = 3
    RULE_conditionalStatement = 4
    RULE_loopingConstruct = 5
    RULE_functionCall = 6
    RULE_returnStatement = 7
    RULE_expression = 8

    ruleNames =  [ "program", "functionDefinition", "statement", "assignment", 
                   "conditionalStatement", "loopingConstruct", "functionCall", 
                   "returnStatement", "expression" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    T__13=14
    T__14=15
    T__15=16
    IDENTIFIER=17
    NAME=18
    STRING=19
    NUMBER=20
    COMMENT=21
    WS=22

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    class ProgramContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(KilianCode303va1Parser.EOF, 0)

        def functionDefinition(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(KilianCode303va1Parser.FunctionDefinitionContext)
            else:
                return self.getTypedRuleContext(KilianCode303va1Parser.FunctionDefinitionContext,i)


        def getRuleIndex(self):
            return KilianCode303va1Parser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)




    def program(self):

        localctx = KilianCode303va1Parser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 21
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==KilianCode303va1Parser.T__0:
                self.state = 18
                self.functionDefinition()
                self.state = 23
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 24
            self.match(KilianCode303va1Parser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class FunctionDefinitionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(KilianCode303va1Parser.IDENTIFIER, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(KilianCode303va1Parser.StatementContext)
            else:
                return self.getTypedRuleContext(KilianCode303va1Parser.StatementContext,i)


        def getRuleIndex(self):
            return KilianCode303va1Parser.RULE_functionDefinition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunctionDefinition" ):
                listener.enterFunctionDefinition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunctionDefinition" ):
                listener.exitFunctionDefinition(self)




    def functionDefinition(self):

        localctx = KilianCode303va1Parser.FunctionDefinitionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_functionDefinition)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 26
            self.match(KilianCode303va1Parser.T__0)
            self.state = 27
            self.match(KilianCode303va1Parser.IDENTIFIER)
            self.state = 31
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << KilianCode303va1Parser.T__2) | (1 << KilianCode303va1Parser.T__4) | (1 << KilianCode303va1Parser.T__5) | (1 << KilianCode303va1Parser.T__7) | (1 << KilianCode303va1Parser.T__8) | (1 << KilianCode303va1Parser.IDENTIFIER))) != 0):
                self.state = 28
                self.statement()
                self.state = 33
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

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assignment(self):
            return self.getTypedRuleContext(KilianCode303va1Parser.AssignmentContext,0)


        def conditionalStatement(self):
            return self.getTypedRuleContext(KilianCode303va1Parser.ConditionalStatementContext,0)


        def loopingConstruct(self):
            return self.getTypedRuleContext(KilianCode303va1Parser.LoopingConstructContext,0)


        def functionCall(self):
            return self.getTypedRuleContext(KilianCode303va1Parser.FunctionCallContext,0)


        def returnStatement(self):
            return self.getTypedRuleContext(KilianCode303va1Parser.ReturnStatementContext,0)


        def getRuleIndex(self):
            return KilianCode303va1Parser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)




    def statement(self):

        localctx = KilianCode303va1Parser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_statement)
        try:
            self.state = 39
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [KilianCode303va1Parser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 34
                self.assignment()
                pass
            elif token in [KilianCode303va1Parser.T__2]:
                self.enterOuterAlt(localctx, 2)
                self.state = 35
                self.conditionalStatement()
                pass
            elif token in [KilianCode303va1Parser.T__4, KilianCode303va1Parser.T__5]:
                self.enterOuterAlt(localctx, 3)
                self.state = 36
                self.loopingConstruct()
                pass
            elif token in [KilianCode303va1Parser.T__7]:
                self.enterOuterAlt(localctx, 4)
                self.state = 37
                self.functionCall()
                pass
            elif token in [KilianCode303va1Parser.T__8]:
                self.enterOuterAlt(localctx, 5)
                self.state = 38
                self.returnStatement()
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

    class AssignmentContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(KilianCode303va1Parser.IDENTIFIER, 0)

        def expression(self):
            return self.getTypedRuleContext(KilianCode303va1Parser.ExpressionContext,0)


        def getRuleIndex(self):
            return KilianCode303va1Parser.RULE_assignment

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignment" ):
                listener.enterAssignment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignment" ):
                listener.exitAssignment(self)




    def assignment(self):

        localctx = KilianCode303va1Parser.AssignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_assignment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 41
            self.match(KilianCode303va1Parser.IDENTIFIER)
            self.state = 42
            self.match(KilianCode303va1Parser.T__1)
            self.state = 43
            self.expression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ConditionalStatementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(KilianCode303va1Parser.ExpressionContext,0)


        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(KilianCode303va1Parser.StatementContext)
            else:
                return self.getTypedRuleContext(KilianCode303va1Parser.StatementContext,i)


        def getRuleIndex(self):
            return KilianCode303va1Parser.RULE_conditionalStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConditionalStatement" ):
                listener.enterConditionalStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConditionalStatement" ):
                listener.exitConditionalStatement(self)




    def conditionalStatement(self):

        localctx = KilianCode303va1Parser.ConditionalStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_conditionalStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 45
            self.match(KilianCode303va1Parser.T__2)
            self.state = 46
            self.expression()
            self.state = 47
            self.statement()
            self.state = 50
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.state = 48
                self.match(KilianCode303va1Parser.T__3)
                self.state = 49
                self.statement()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class LoopingConstructContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(KilianCode303va1Parser.ExpressionContext,0)


        def statement(self):
            return self.getTypedRuleContext(KilianCode303va1Parser.StatementContext,0)


        def IDENTIFIER(self):
            return self.getToken(KilianCode303va1Parser.IDENTIFIER, 0)

        def getRuleIndex(self):
            return KilianCode303va1Parser.RULE_loopingConstruct

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLoopingConstruct" ):
                listener.enterLoopingConstruct(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLoopingConstruct" ):
                listener.exitLoopingConstruct(self)




    def loopingConstruct(self):

        localctx = KilianCode303va1Parser.LoopingConstructContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_loopingConstruct)
        try:
            self.state = 62
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [KilianCode303va1Parser.T__4]:
                self.enterOuterAlt(localctx, 1)
                self.state = 52
                self.match(KilianCode303va1Parser.T__4)
                self.state = 53
                self.expression()
                self.state = 54
                self.statement()
                pass
            elif token in [KilianCode303va1Parser.T__5]:
                self.enterOuterAlt(localctx, 2)
                self.state = 56
                self.match(KilianCode303va1Parser.T__5)
                self.state = 57
                self.match(KilianCode303va1Parser.IDENTIFIER)
                self.state = 58
                self.match(KilianCode303va1Parser.T__6)
                self.state = 59
                self.expression()
                self.state = 60
                self.statement()
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

    class FunctionCallContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(KilianCode303va1Parser.IDENTIFIER, 0)

        def getRuleIndex(self):
            return KilianCode303va1Parser.RULE_functionCall

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunctionCall" ):
                listener.enterFunctionCall(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunctionCall" ):
                listener.exitFunctionCall(self)




    def functionCall(self):

        localctx = KilianCode303va1Parser.FunctionCallContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_functionCall)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 64
            self.match(KilianCode303va1Parser.T__7)
            self.state = 65
            self.match(KilianCode303va1Parser.IDENTIFIER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ReturnStatementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(KilianCode303va1Parser.ExpressionContext,0)


        def getRuleIndex(self):
            return KilianCode303va1Parser.RULE_returnStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterReturnStatement" ):
                listener.enterReturnStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitReturnStatement" ):
                listener.exitReturnStatement(self)




    def returnStatement(self):

        localctx = KilianCode303va1Parser.ReturnStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_returnStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 67
            self.match(KilianCode303va1Parser.T__8)
            self.state = 68
            self.expression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ExpressionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self, i:int=None):
            if i is None:
                return self.getTokens(KilianCode303va1Parser.IDENTIFIER)
            else:
                return self.getToken(KilianCode303va1Parser.IDENTIFIER, i)

        def STRING(self):
            return self.getToken(KilianCode303va1Parser.STRING, 0)

        def NUMBER(self):
            return self.getToken(KilianCode303va1Parser.NUMBER, 0)

        def getRuleIndex(self):
            return KilianCode303va1Parser.RULE_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpression" ):
                listener.enterExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpression" ):
                listener.exitExpression(self)




    def expression(self):

        localctx = KilianCode303va1Parser.ExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_expression)
        self._la = 0 # Token type
        try:
            self.state = 76
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 70
                self.match(KilianCode303va1Parser.IDENTIFIER)
                self.state = 71
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << KilianCode303va1Parser.T__9) | (1 << KilianCode303va1Parser.T__10) | (1 << KilianCode303va1Parser.T__11) | (1 << KilianCode303va1Parser.T__12) | (1 << KilianCode303va1Parser.T__13) | (1 << KilianCode303va1Parser.T__14) | (1 << KilianCode303va1Parser.T__15))) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 72
                self.match(KilianCode303va1Parser.IDENTIFIER)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 73
                self.match(KilianCode303va1Parser.IDENTIFIER)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 74
                self.match(KilianCode303va1Parser.STRING)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 75
                self.match(KilianCode303va1Parser.NUMBER)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





