# Generated from calculusparser.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,48,222,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,1,0,4,0,26,8,0,11,
        0,12,0,27,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
        1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3,1,53,8,1,1,2,1,2,1,2,1,2,
        1,2,1,2,1,2,1,2,1,2,5,2,64,8,2,10,2,12,2,67,9,2,1,3,1,3,1,3,1,3,
        1,3,1,3,1,3,1,3,1,3,5,3,78,8,3,10,3,12,3,81,9,3,1,4,1,4,1,4,1,4,
        1,4,3,4,88,8,4,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,
        5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,
        5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,
        5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,
        5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,3,
        5,166,8,5,1,6,1,6,1,6,1,6,1,6,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,
        7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,3,7,190,8,7,1,8,1,8,1,8,1,8,1,
        8,1,8,1,8,1,8,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,10,1,10,1,10,1,10,1,
        10,1,10,1,10,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,0,2,4,
        6,12,0,2,4,6,8,10,12,14,16,18,20,22,0,1,1,0,15,16,239,0,25,1,0,0,
        0,2,52,1,0,0,0,4,54,1,0,0,0,6,68,1,0,0,0,8,87,1,0,0,0,10,165,1,0,
        0,0,12,167,1,0,0,0,14,189,1,0,0,0,16,191,1,0,0,0,18,199,1,0,0,0,
        20,206,1,0,0,0,22,213,1,0,0,0,24,26,3,2,1,0,25,24,1,0,0,0,26,27,
        1,0,0,0,27,25,1,0,0,0,27,28,1,0,0,0,28,29,1,0,0,0,29,30,5,0,0,1,
        30,1,1,0,0,0,31,32,3,4,2,0,32,33,5,24,0,0,33,53,1,0,0,0,34,35,3,
        12,6,0,35,36,5,24,0,0,36,53,1,0,0,0,37,38,3,14,7,0,38,39,5,24,0,
        0,39,53,1,0,0,0,40,41,3,18,9,0,41,42,5,24,0,0,42,53,1,0,0,0,43,44,
        3,16,8,0,44,45,5,24,0,0,45,53,1,0,0,0,46,47,3,20,10,0,47,48,5,24,
        0,0,48,53,1,0,0,0,49,50,3,22,11,0,50,51,5,24,0,0,51,53,1,0,0,0,52,
        31,1,0,0,0,52,34,1,0,0,0,52,37,1,0,0,0,52,40,1,0,0,0,52,43,1,0,0,
        0,52,46,1,0,0,0,52,49,1,0,0,0,53,3,1,0,0,0,54,55,6,2,-1,0,55,56,
        3,6,3,0,56,65,1,0,0,0,57,58,10,3,0,0,58,59,5,9,0,0,59,64,3,6,3,0,
        60,61,10,2,0,0,61,62,5,10,0,0,62,64,3,6,3,0,63,57,1,0,0,0,63,60,
        1,0,0,0,64,67,1,0,0,0,65,63,1,0,0,0,65,66,1,0,0,0,66,5,1,0,0,0,67,
        65,1,0,0,0,68,69,6,3,-1,0,69,70,3,8,4,0,70,79,1,0,0,0,71,72,10,3,
        0,0,72,73,5,11,0,0,73,78,3,8,4,0,74,75,10,2,0,0,75,76,5,12,0,0,76,
        78,3,8,4,0,77,71,1,0,0,0,77,74,1,0,0,0,78,81,1,0,0,0,79,77,1,0,0,
        0,79,80,1,0,0,0,80,7,1,0,0,0,81,79,1,0,0,0,82,83,3,10,5,0,83,84,
        5,13,0,0,84,85,3,8,4,0,85,88,1,0,0,0,86,88,3,10,5,0,87,82,1,0,0,
        0,87,86,1,0,0,0,88,9,1,0,0,0,89,166,5,44,0,0,90,166,5,45,0,0,91,
        92,5,25,0,0,92,93,5,17,0,0,93,94,3,4,2,0,94,95,5,18,0,0,95,166,1,
        0,0,0,96,97,5,26,0,0,97,98,5,17,0,0,98,99,3,4,2,0,99,100,5,18,0,
        0,100,166,1,0,0,0,101,102,5,27,0,0,102,103,5,17,0,0,103,104,3,4,
        2,0,104,105,5,18,0,0,105,166,1,0,0,0,106,107,5,28,0,0,107,108,5,
        17,0,0,108,109,3,4,2,0,109,110,5,18,0,0,110,166,1,0,0,0,111,112,
        5,29,0,0,112,113,5,17,0,0,113,114,3,4,2,0,114,115,5,18,0,0,115,166,
        1,0,0,0,116,117,5,30,0,0,117,118,5,17,0,0,118,119,3,4,2,0,119,120,
        5,18,0,0,120,166,1,0,0,0,121,122,5,31,0,0,122,123,5,17,0,0,123,124,
        3,4,2,0,124,125,5,18,0,0,125,166,1,0,0,0,126,127,5,32,0,0,127,128,
        5,17,0,0,128,129,3,4,2,0,129,130,5,18,0,0,130,166,1,0,0,0,131,132,
        5,33,0,0,132,133,5,17,0,0,133,134,3,4,2,0,134,135,5,18,0,0,135,166,
        1,0,0,0,136,137,5,34,0,0,137,138,5,17,0,0,138,139,3,4,2,0,139,140,
        5,18,0,0,140,166,1,0,0,0,141,142,5,35,0,0,142,143,5,17,0,0,143,144,
        3,4,2,0,144,145,5,18,0,0,145,166,1,0,0,0,146,147,5,36,0,0,147,148,
        5,17,0,0,148,149,3,4,2,0,149,150,5,18,0,0,150,166,1,0,0,0,151,152,
        5,37,0,0,152,153,5,17,0,0,153,154,3,4,2,0,154,155,5,18,0,0,155,166,
        1,0,0,0,156,157,5,38,0,0,157,158,5,17,0,0,158,159,3,4,2,0,159,160,
        5,18,0,0,160,166,1,0,0,0,161,162,5,17,0,0,162,163,3,4,2,0,163,164,
        5,18,0,0,164,166,1,0,0,0,165,89,1,0,0,0,165,90,1,0,0,0,165,91,1,
        0,0,0,165,96,1,0,0,0,165,101,1,0,0,0,165,106,1,0,0,0,165,111,1,0,
        0,0,165,116,1,0,0,0,165,121,1,0,0,0,165,126,1,0,0,0,165,131,1,0,
        0,0,165,136,1,0,0,0,165,141,1,0,0,0,165,146,1,0,0,0,165,151,1,0,
        0,0,165,156,1,0,0,0,165,161,1,0,0,0,166,11,1,0,0,0,167,168,5,1,0,
        0,168,169,3,4,2,0,169,170,5,3,0,0,170,171,5,45,0,0,171,13,1,0,0,
        0,172,173,5,4,0,0,173,174,5,17,0,0,174,175,5,45,0,0,175,176,5,18,
        0,0,176,177,5,14,0,0,177,190,3,4,2,0,178,179,5,5,0,0,179,180,5,17,
        0,0,180,181,5,45,0,0,181,182,5,18,0,0,182,183,5,14,0,0,183,190,3,
        4,2,0,184,185,5,8,0,0,185,186,5,17,0,0,186,187,5,45,0,0,187,188,
        5,18,0,0,188,190,3,4,2,0,189,172,1,0,0,0,189,178,1,0,0,0,189,184,
        1,0,0,0,190,15,1,0,0,0,191,192,5,2,0,0,192,193,5,45,0,0,193,194,
        5,12,0,0,194,195,5,2,0,0,195,196,5,45,0,0,196,197,5,14,0,0,197,198,
        3,4,2,0,198,17,1,0,0,0,199,200,5,45,0,0,200,201,5,17,0,0,201,202,
        3,4,2,0,202,203,5,18,0,0,203,204,7,0,0,0,204,205,3,4,2,0,205,19,
        1,0,0,0,206,207,5,45,0,0,207,208,5,17,0,0,208,209,5,45,0,0,209,210,
        5,18,0,0,210,211,5,14,0,0,211,212,3,4,2,0,212,21,1,0,0,0,213,214,
        5,39,0,0,214,215,5,19,0,0,215,216,5,45,0,0,216,217,5,42,0,0,217,
        218,3,4,2,0,218,219,5,20,0,0,219,220,3,4,2,0,220,23,1,0,0,0,9,27,
        52,63,65,77,79,87,165,189
    ]

class calculusparser ( Parser ):

    grammarFileName = "calculusparser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'\\u222B'", "'\\u2202'", "'d'", "'''", 
                     "'d2'", "'dt'", "'dx'", "'ddx'", "'+'", "'-'", "'*'", 
                     "'/'", "'^'", "'='", "':'", "'|'", "'('", "')'", "'{'", 
                     "'}'", "'['", "']'", "','", "';'", "'sen'", "'cos'", 
                     "'tan'", "'cot'", "'sec'", "'csc'", "'arcsen'", "'arccos'", 
                     "'arctan'", "'ln'", "'log'", "'exp'", "'sqrt'", "'abs'", 
                     "'lim'", "'pi'", "'e'", "'->'" ]

    symbolicNames = [ "<INVALID>", "INTEGRAL", "DERIVADAP", "DIFERENCIAL", 
                      "DERIVADAPRIMA", "SEGUNDADERIVADA", "DT", "DX", "DDX", 
                      "SUMA", "RESTA", "MULTI", "DIV", "POTE", "IGUAL", 
                      "COLON", "BARRA", "LPAREN", "RPAREN", "LBRACE", "RBRACE", 
                      "LBRACK", "RBRACK", "COMA", "SEMICO", "SIN", "COS", 
                      "TAN", "COT", "SEC", "CSC", "ARCSIN", "ARCCOS", "ARCTAN", 
                      "LN", "LOG", "EXP", "SQRT", "ABS", "LIMIT", "PI", 
                      "ECONST", "ARROW", "DIGIT", "NUMBER", "ID", "WS", 
                      "COMENTARIO", "LINEACOMENT" ]

    RULE_prog = 0
    RULE_stat = 1
    RULE_expr = 2
    RULE_term = 3
    RULE_factor = 4
    RULE_atom = 5
    RULE_integralStmt = 6
    RULE_differentialEq = 7
    RULE_partialEq = 8
    RULE_initCond = 9
    RULE_funcDef = 10
    RULE_limitStmt = 11

    ruleNames =  [ "prog", "stat", "expr", "term", "factor", "atom", "integralStmt", 
                   "differentialEq", "partialEq", "initCond", "funcDef", 
                   "limitStmt" ]

    EOF = Token.EOF
    INTEGRAL=1
    DERIVADAP=2
    DIFERENCIAL=3
    DERIVADAPRIMA=4
    SEGUNDADERIVADA=5
    DT=6
    DX=7
    DDX=8
    SUMA=9
    RESTA=10
    MULTI=11
    DIV=12
    POTE=13
    IGUAL=14
    COLON=15
    BARRA=16
    LPAREN=17
    RPAREN=18
    LBRACE=19
    RBRACE=20
    LBRACK=21
    RBRACK=22
    COMA=23
    SEMICO=24
    SIN=25
    COS=26
    TAN=27
    COT=28
    SEC=29
    CSC=30
    ARCSIN=31
    ARCCOS=32
    ARCTAN=33
    LN=34
    LOG=35
    EXP=36
    SQRT=37
    ABS=38
    LIMIT=39
    PI=40
    ECONST=41
    ARROW=42
    DIGIT=43
    NUMBER=44
    ID=45
    WS=46
    COMENTARIO=47
    LINEACOMENT=48

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(calculusparser.EOF, 0)

        def stat(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(calculusparser.StatContext)
            else:
                return self.getTypedRuleContext(calculusparser.StatContext,i)


        def getRuleIndex(self):
            return calculusparser.RULE_prog

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProg" ):
                listener.enterProg(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProg" ):
                listener.exitProg(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProg" ):
                return visitor.visitProg(self)
            else:
                return visitor.visitChildren(self)




    def prog(self):

        localctx = calculusparser.ProgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_prog)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 25 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 24
                self.stat()
                self.state = 27 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 53876036337974) != 0)):
                    break

            self.state = 29
            self.match(calculusparser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(calculusparser.ExprContext,0)


        def SEMICO(self):
            return self.getToken(calculusparser.SEMICO, 0)

        def integralStmt(self):
            return self.getTypedRuleContext(calculusparser.IntegralStmtContext,0)


        def differentialEq(self):
            return self.getTypedRuleContext(calculusparser.DifferentialEqContext,0)


        def initCond(self):
            return self.getTypedRuleContext(calculusparser.InitCondContext,0)


        def partialEq(self):
            return self.getTypedRuleContext(calculusparser.PartialEqContext,0)


        def funcDef(self):
            return self.getTypedRuleContext(calculusparser.FuncDefContext,0)


        def limitStmt(self):
            return self.getTypedRuleContext(calculusparser.LimitStmtContext,0)


        def getRuleIndex(self):
            return calculusparser.RULE_stat

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStat" ):
                listener.enterStat(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStat" ):
                listener.exitStat(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStat" ):
                return visitor.visitStat(self)
            else:
                return visitor.visitChildren(self)




    def stat(self):

        localctx = calculusparser.StatContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_stat)
        try:
            self.state = 52
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 31
                self.expr(0)
                self.state = 32
                self.match(calculusparser.SEMICO)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 34
                self.integralStmt()
                self.state = 35
                self.match(calculusparser.SEMICO)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 37
                self.differentialEq()
                self.state = 38
                self.match(calculusparser.SEMICO)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 40
                self.initCond()
                self.state = 41
                self.match(calculusparser.SEMICO)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 43
                self.partialEq()
                self.state = 44
                self.match(calculusparser.SEMICO)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 46
                self.funcDef()
                self.state = 47
                self.match(calculusparser.SEMICO)
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 49
                self.limitStmt()
                self.state = 50
                self.match(calculusparser.SEMICO)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def term(self):
            return self.getTypedRuleContext(calculusparser.TermContext,0)


        def expr(self):
            return self.getTypedRuleContext(calculusparser.ExprContext,0)


        def SUMA(self):
            return self.getToken(calculusparser.SUMA, 0)

        def RESTA(self):
            return self.getToken(calculusparser.RESTA, 0)

        def getRuleIndex(self):
            return calculusparser.RULE_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr" ):
                listener.enterExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr" ):
                listener.exitExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr" ):
                return visitor.visitExpr(self)
            else:
                return visitor.visitChildren(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = calculusparser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 4
        self.enterRecursionRule(localctx, 4, self.RULE_expr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 55
            self.term(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 65
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,3,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 63
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
                    if la_ == 1:
                        localctx = calculusparser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 57
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 58
                        self.match(calculusparser.SUMA)
                        self.state = 59
                        self.term(0)
                        pass

                    elif la_ == 2:
                        localctx = calculusparser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 60
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 61
                        self.match(calculusparser.RESTA)
                        self.state = 62
                        self.term(0)
                        pass

             
                self.state = 67
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,3,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class TermContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def factor(self):
            return self.getTypedRuleContext(calculusparser.FactorContext,0)


        def term(self):
            return self.getTypedRuleContext(calculusparser.TermContext,0)


        def MULTI(self):
            return self.getToken(calculusparser.MULTI, 0)

        def DIV(self):
            return self.getToken(calculusparser.DIV, 0)

        def getRuleIndex(self):
            return calculusparser.RULE_term

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTerm" ):
                listener.enterTerm(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTerm" ):
                listener.exitTerm(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTerm" ):
                return visitor.visitTerm(self)
            else:
                return visitor.visitChildren(self)



    def term(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = calculusparser.TermContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 6
        self.enterRecursionRule(localctx, 6, self.RULE_term, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 69
            self.factor()
            self._ctx.stop = self._input.LT(-1)
            self.state = 79
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,5,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 77
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
                    if la_ == 1:
                        localctx = calculusparser.TermContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_term)
                        self.state = 71
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 72
                        self.match(calculusparser.MULTI)
                        self.state = 73
                        self.factor()
                        pass

                    elif la_ == 2:
                        localctx = calculusparser.TermContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_term)
                        self.state = 74
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 75
                        self.match(calculusparser.DIV)
                        self.state = 76
                        self.factor()
                        pass

             
                self.state = 81
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,5,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class FactorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def atom(self):
            return self.getTypedRuleContext(calculusparser.AtomContext,0)


        def POTE(self):
            return self.getToken(calculusparser.POTE, 0)

        def factor(self):
            return self.getTypedRuleContext(calculusparser.FactorContext,0)


        def getRuleIndex(self):
            return calculusparser.RULE_factor

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFactor" ):
                listener.enterFactor(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFactor" ):
                listener.exitFactor(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFactor" ):
                return visitor.visitFactor(self)
            else:
                return visitor.visitChildren(self)




    def factor(self):

        localctx = calculusparser.FactorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_factor)
        try:
            self.state = 87
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 82
                self.atom()
                self.state = 83
                self.match(calculusparser.POTE)
                self.state = 84
                self.factor()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 86
                self.atom()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AtomContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMBER(self):
            return self.getToken(calculusparser.NUMBER, 0)

        def ID(self):
            return self.getToken(calculusparser.ID, 0)

        def SIN(self):
            return self.getToken(calculusparser.SIN, 0)

        def LPAREN(self):
            return self.getToken(calculusparser.LPAREN, 0)

        def expr(self):
            return self.getTypedRuleContext(calculusparser.ExprContext,0)


        def RPAREN(self):
            return self.getToken(calculusparser.RPAREN, 0)

        def COS(self):
            return self.getToken(calculusparser.COS, 0)

        def TAN(self):
            return self.getToken(calculusparser.TAN, 0)

        def COT(self):
            return self.getToken(calculusparser.COT, 0)

        def SEC(self):
            return self.getToken(calculusparser.SEC, 0)

        def CSC(self):
            return self.getToken(calculusparser.CSC, 0)

        def ARCSIN(self):
            return self.getToken(calculusparser.ARCSIN, 0)

        def ARCCOS(self):
            return self.getToken(calculusparser.ARCCOS, 0)

        def ARCTAN(self):
            return self.getToken(calculusparser.ARCTAN, 0)

        def LN(self):
            return self.getToken(calculusparser.LN, 0)

        def LOG(self):
            return self.getToken(calculusparser.LOG, 0)

        def EXP(self):
            return self.getToken(calculusparser.EXP, 0)

        def SQRT(self):
            return self.getToken(calculusparser.SQRT, 0)

        def ABS(self):
            return self.getToken(calculusparser.ABS, 0)

        def getRuleIndex(self):
            return calculusparser.RULE_atom

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAtom" ):
                listener.enterAtom(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAtom" ):
                listener.exitAtom(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAtom" ):
                return visitor.visitAtom(self)
            else:
                return visitor.visitChildren(self)




    def atom(self):

        localctx = calculusparser.AtomContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_atom)
        try:
            self.state = 165
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [44]:
                self.enterOuterAlt(localctx, 1)
                self.state = 89
                self.match(calculusparser.NUMBER)
                pass
            elif token in [45]:
                self.enterOuterAlt(localctx, 2)
                self.state = 90
                self.match(calculusparser.ID)
                pass
            elif token in [25]:
                self.enterOuterAlt(localctx, 3)
                self.state = 91
                self.match(calculusparser.SIN)
                self.state = 92
                self.match(calculusparser.LPAREN)
                self.state = 93
                self.expr(0)
                self.state = 94
                self.match(calculusparser.RPAREN)
                pass
            elif token in [26]:
                self.enterOuterAlt(localctx, 4)
                self.state = 96
                self.match(calculusparser.COS)
                self.state = 97
                self.match(calculusparser.LPAREN)
                self.state = 98
                self.expr(0)
                self.state = 99
                self.match(calculusparser.RPAREN)
                pass
            elif token in [27]:
                self.enterOuterAlt(localctx, 5)
                self.state = 101
                self.match(calculusparser.TAN)
                self.state = 102
                self.match(calculusparser.LPAREN)
                self.state = 103
                self.expr(0)
                self.state = 104
                self.match(calculusparser.RPAREN)
                pass
            elif token in [28]:
                self.enterOuterAlt(localctx, 6)
                self.state = 106
                self.match(calculusparser.COT)
                self.state = 107
                self.match(calculusparser.LPAREN)
                self.state = 108
                self.expr(0)
                self.state = 109
                self.match(calculusparser.RPAREN)
                pass
            elif token in [29]:
                self.enterOuterAlt(localctx, 7)
                self.state = 111
                self.match(calculusparser.SEC)
                self.state = 112
                self.match(calculusparser.LPAREN)
                self.state = 113
                self.expr(0)
                self.state = 114
                self.match(calculusparser.RPAREN)
                pass
            elif token in [30]:
                self.enterOuterAlt(localctx, 8)
                self.state = 116
                self.match(calculusparser.CSC)
                self.state = 117
                self.match(calculusparser.LPAREN)
                self.state = 118
                self.expr(0)
                self.state = 119
                self.match(calculusparser.RPAREN)
                pass
            elif token in [31]:
                self.enterOuterAlt(localctx, 9)
                self.state = 121
                self.match(calculusparser.ARCSIN)
                self.state = 122
                self.match(calculusparser.LPAREN)
                self.state = 123
                self.expr(0)
                self.state = 124
                self.match(calculusparser.RPAREN)
                pass
            elif token in [32]:
                self.enterOuterAlt(localctx, 10)
                self.state = 126
                self.match(calculusparser.ARCCOS)
                self.state = 127
                self.match(calculusparser.LPAREN)
                self.state = 128
                self.expr(0)
                self.state = 129
                self.match(calculusparser.RPAREN)
                pass
            elif token in [33]:
                self.enterOuterAlt(localctx, 11)
                self.state = 131
                self.match(calculusparser.ARCTAN)
                self.state = 132
                self.match(calculusparser.LPAREN)
                self.state = 133
                self.expr(0)
                self.state = 134
                self.match(calculusparser.RPAREN)
                pass
            elif token in [34]:
                self.enterOuterAlt(localctx, 12)
                self.state = 136
                self.match(calculusparser.LN)
                self.state = 137
                self.match(calculusparser.LPAREN)
                self.state = 138
                self.expr(0)
                self.state = 139
                self.match(calculusparser.RPAREN)
                pass
            elif token in [35]:
                self.enterOuterAlt(localctx, 13)
                self.state = 141
                self.match(calculusparser.LOG)
                self.state = 142
                self.match(calculusparser.LPAREN)
                self.state = 143
                self.expr(0)
                self.state = 144
                self.match(calculusparser.RPAREN)
                pass
            elif token in [36]:
                self.enterOuterAlt(localctx, 14)
                self.state = 146
                self.match(calculusparser.EXP)
                self.state = 147
                self.match(calculusparser.LPAREN)
                self.state = 148
                self.expr(0)
                self.state = 149
                self.match(calculusparser.RPAREN)
                pass
            elif token in [37]:
                self.enterOuterAlt(localctx, 15)
                self.state = 151
                self.match(calculusparser.SQRT)
                self.state = 152
                self.match(calculusparser.LPAREN)
                self.state = 153
                self.expr(0)
                self.state = 154
                self.match(calculusparser.RPAREN)
                pass
            elif token in [38]:
                self.enterOuterAlt(localctx, 16)
                self.state = 156
                self.match(calculusparser.ABS)
                self.state = 157
                self.match(calculusparser.LPAREN)
                self.state = 158
                self.expr(0)
                self.state = 159
                self.match(calculusparser.RPAREN)
                pass
            elif token in [17]:
                self.enterOuterAlt(localctx, 17)
                self.state = 161
                self.match(calculusparser.LPAREN)
                self.state = 162
                self.expr(0)
                self.state = 163
                self.match(calculusparser.RPAREN)
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


    class IntegralStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTEGRAL(self):
            return self.getToken(calculusparser.INTEGRAL, 0)

        def expr(self):
            return self.getTypedRuleContext(calculusparser.ExprContext,0)


        def DIFERENCIAL(self):
            return self.getToken(calculusparser.DIFERENCIAL, 0)

        def ID(self):
            return self.getToken(calculusparser.ID, 0)

        def getRuleIndex(self):
            return calculusparser.RULE_integralStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIntegralStmt" ):
                listener.enterIntegralStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIntegralStmt" ):
                listener.exitIntegralStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIntegralStmt" ):
                return visitor.visitIntegralStmt(self)
            else:
                return visitor.visitChildren(self)




    def integralStmt(self):

        localctx = calculusparser.IntegralStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_integralStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 167
            self.match(calculusparser.INTEGRAL)
            self.state = 168
            self.expr(0)
            self.state = 169
            self.match(calculusparser.DIFERENCIAL)
            self.state = 170
            self.match(calculusparser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DifferentialEqContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DERIVADAPRIMA(self):
            return self.getToken(calculusparser.DERIVADAPRIMA, 0)

        def LPAREN(self):
            return self.getToken(calculusparser.LPAREN, 0)

        def ID(self):
            return self.getToken(calculusparser.ID, 0)

        def RPAREN(self):
            return self.getToken(calculusparser.RPAREN, 0)

        def IGUAL(self):
            return self.getToken(calculusparser.IGUAL, 0)

        def expr(self):
            return self.getTypedRuleContext(calculusparser.ExprContext,0)


        def SEGUNDADERIVADA(self):
            return self.getToken(calculusparser.SEGUNDADERIVADA, 0)

        def DDX(self):
            return self.getToken(calculusparser.DDX, 0)

        def getRuleIndex(self):
            return calculusparser.RULE_differentialEq

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDifferentialEq" ):
                listener.enterDifferentialEq(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDifferentialEq" ):
                listener.exitDifferentialEq(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDifferentialEq" ):
                return visitor.visitDifferentialEq(self)
            else:
                return visitor.visitChildren(self)




    def differentialEq(self):

        localctx = calculusparser.DifferentialEqContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_differentialEq)
        try:
            self.state = 189
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [4]:
                self.enterOuterAlt(localctx, 1)
                self.state = 172
                self.match(calculusparser.DERIVADAPRIMA)
                self.state = 173
                self.match(calculusparser.LPAREN)
                self.state = 174
                self.match(calculusparser.ID)
                self.state = 175
                self.match(calculusparser.RPAREN)
                self.state = 176
                self.match(calculusparser.IGUAL)
                self.state = 177
                self.expr(0)
                pass
            elif token in [5]:
                self.enterOuterAlt(localctx, 2)
                self.state = 178
                self.match(calculusparser.SEGUNDADERIVADA)
                self.state = 179
                self.match(calculusparser.LPAREN)
                self.state = 180
                self.match(calculusparser.ID)
                self.state = 181
                self.match(calculusparser.RPAREN)
                self.state = 182
                self.match(calculusparser.IGUAL)
                self.state = 183
                self.expr(0)
                pass
            elif token in [8]:
                self.enterOuterAlt(localctx, 3)
                self.state = 184
                self.match(calculusparser.DDX)
                self.state = 185
                self.match(calculusparser.LPAREN)
                self.state = 186
                self.match(calculusparser.ID)
                self.state = 187
                self.match(calculusparser.RPAREN)
                self.state = 188
                self.expr(0)
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


    class PartialEqContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DERIVADAP(self, i:int=None):
            if i is None:
                return self.getTokens(calculusparser.DERIVADAP)
            else:
                return self.getToken(calculusparser.DERIVADAP, i)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(calculusparser.ID)
            else:
                return self.getToken(calculusparser.ID, i)

        def DIV(self):
            return self.getToken(calculusparser.DIV, 0)

        def IGUAL(self):
            return self.getToken(calculusparser.IGUAL, 0)

        def expr(self):
            return self.getTypedRuleContext(calculusparser.ExprContext,0)


        def getRuleIndex(self):
            return calculusparser.RULE_partialEq

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPartialEq" ):
                listener.enterPartialEq(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPartialEq" ):
                listener.exitPartialEq(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPartialEq" ):
                return visitor.visitPartialEq(self)
            else:
                return visitor.visitChildren(self)




    def partialEq(self):

        localctx = calculusparser.PartialEqContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_partialEq)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 191
            self.match(calculusparser.DERIVADAP)
            self.state = 192
            self.match(calculusparser.ID)
            self.state = 193
            self.match(calculusparser.DIV)
            self.state = 194
            self.match(calculusparser.DERIVADAP)
            self.state = 195
            self.match(calculusparser.ID)
            self.state = 196
            self.match(calculusparser.IGUAL)
            self.state = 197
            self.expr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InitCondContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(calculusparser.ID, 0)

        def LPAREN(self):
            return self.getToken(calculusparser.LPAREN, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(calculusparser.ExprContext)
            else:
                return self.getTypedRuleContext(calculusparser.ExprContext,i)


        def RPAREN(self):
            return self.getToken(calculusparser.RPAREN, 0)

        def COLON(self):
            return self.getToken(calculusparser.COLON, 0)

        def BARRA(self):
            return self.getToken(calculusparser.BARRA, 0)

        def getRuleIndex(self):
            return calculusparser.RULE_initCond

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInitCond" ):
                listener.enterInitCond(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInitCond" ):
                listener.exitInitCond(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInitCond" ):
                return visitor.visitInitCond(self)
            else:
                return visitor.visitChildren(self)




    def initCond(self):

        localctx = calculusparser.InitCondContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_initCond)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 199
            self.match(calculusparser.ID)
            self.state = 200
            self.match(calculusparser.LPAREN)
            self.state = 201
            self.expr(0)
            self.state = 202
            self.match(calculusparser.RPAREN)
            self.state = 203
            _la = self._input.LA(1)
            if not(_la==15 or _la==16):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 204
            self.expr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FuncDefContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(calculusparser.ID)
            else:
                return self.getToken(calculusparser.ID, i)

        def LPAREN(self):
            return self.getToken(calculusparser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(calculusparser.RPAREN, 0)

        def IGUAL(self):
            return self.getToken(calculusparser.IGUAL, 0)

        def expr(self):
            return self.getTypedRuleContext(calculusparser.ExprContext,0)


        def getRuleIndex(self):
            return calculusparser.RULE_funcDef

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFuncDef" ):
                listener.enterFuncDef(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFuncDef" ):
                listener.exitFuncDef(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFuncDef" ):
                return visitor.visitFuncDef(self)
            else:
                return visitor.visitChildren(self)




    def funcDef(self):

        localctx = calculusparser.FuncDefContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_funcDef)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 206
            self.match(calculusparser.ID)
            self.state = 207
            self.match(calculusparser.LPAREN)
            self.state = 208
            self.match(calculusparser.ID)
            self.state = 209
            self.match(calculusparser.RPAREN)
            self.state = 210
            self.match(calculusparser.IGUAL)
            self.state = 211
            self.expr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LimitStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LIMIT(self):
            return self.getToken(calculusparser.LIMIT, 0)

        def LBRACE(self):
            return self.getToken(calculusparser.LBRACE, 0)

        def ID(self):
            return self.getToken(calculusparser.ID, 0)

        def ARROW(self):
            return self.getToken(calculusparser.ARROW, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(calculusparser.ExprContext)
            else:
                return self.getTypedRuleContext(calculusparser.ExprContext,i)


        def RBRACE(self):
            return self.getToken(calculusparser.RBRACE, 0)

        def getRuleIndex(self):
            return calculusparser.RULE_limitStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLimitStmt" ):
                listener.enterLimitStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLimitStmt" ):
                listener.exitLimitStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLimitStmt" ):
                return visitor.visitLimitStmt(self)
            else:
                return visitor.visitChildren(self)




    def limitStmt(self):

        localctx = calculusparser.LimitStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_limitStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 213
            self.match(calculusparser.LIMIT)
            self.state = 214
            self.match(calculusparser.LBRACE)
            self.state = 215
            self.match(calculusparser.ID)
            self.state = 216
            self.match(calculusparser.ARROW)
            self.state = 217
            self.expr(0)
            self.state = 218
            self.match(calculusparser.RBRACE)
            self.state = 219
            self.expr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[2] = self.expr_sempred
        self._predicates[3] = self.term_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         

    def term_sempred(self, localctx:TermContext, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 2)
         




