# Generated from calculusparser.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .calculusparser import calculusparser
else:
    from calculusparser import calculusparser

# This class defines a complete listener for a parse tree produced by calculusparser.
class calculusparserListener(ParseTreeListener):

    # Enter a parse tree produced by calculusparser#prog.
    def enterProg(self, ctx:calculusparser.ProgContext):
        pass

    # Exit a parse tree produced by calculusparser#prog.
    def exitProg(self, ctx:calculusparser.ProgContext):
        pass


    # Enter a parse tree produced by calculusparser#stat.
    def enterStat(self, ctx:calculusparser.StatContext):
        pass

    # Exit a parse tree produced by calculusparser#stat.
    def exitStat(self, ctx:calculusparser.StatContext):
        pass


    # Enter a parse tree produced by calculusparser#expr.
    def enterExpr(self, ctx:calculusparser.ExprContext):
        pass

    # Exit a parse tree produced by calculusparser#expr.
    def exitExpr(self, ctx:calculusparser.ExprContext):
        pass


    # Enter a parse tree produced by calculusparser#term.
    def enterTerm(self, ctx:calculusparser.TermContext):
        pass

    # Exit a parse tree produced by calculusparser#term.
    def exitTerm(self, ctx:calculusparser.TermContext):
        pass


    # Enter a parse tree produced by calculusparser#factor.
    def enterFactor(self, ctx:calculusparser.FactorContext):
        pass

    # Exit a parse tree produced by calculusparser#factor.
    def exitFactor(self, ctx:calculusparser.FactorContext):
        pass


    # Enter a parse tree produced by calculusparser#atom.
    def enterAtom(self, ctx:calculusparser.AtomContext):
        pass

    # Exit a parse tree produced by calculusparser#atom.
    def exitAtom(self, ctx:calculusparser.AtomContext):
        pass


    # Enter a parse tree produced by calculusparser#integralStmt.
    def enterIntegralStmt(self, ctx:calculusparser.IntegralStmtContext):
        pass

    # Exit a parse tree produced by calculusparser#integralStmt.
    def exitIntegralStmt(self, ctx:calculusparser.IntegralStmtContext):
        pass


    # Enter a parse tree produced by calculusparser#differentialEq.
    def enterDifferentialEq(self, ctx:calculusparser.DifferentialEqContext):
        pass

    # Exit a parse tree produced by calculusparser#differentialEq.
    def exitDifferentialEq(self, ctx:calculusparser.DifferentialEqContext):
        pass


    # Enter a parse tree produced by calculusparser#partialEq.
    def enterPartialEq(self, ctx:calculusparser.PartialEqContext):
        pass

    # Exit a parse tree produced by calculusparser#partialEq.
    def exitPartialEq(self, ctx:calculusparser.PartialEqContext):
        pass


    # Enter a parse tree produced by calculusparser#initCond.
    def enterInitCond(self, ctx:calculusparser.InitCondContext):
        pass

    # Exit a parse tree produced by calculusparser#initCond.
    def exitInitCond(self, ctx:calculusparser.InitCondContext):
        pass


    # Enter a parse tree produced by calculusparser#funcDef.
    def enterFuncDef(self, ctx:calculusparser.FuncDefContext):
        pass

    # Exit a parse tree produced by calculusparser#funcDef.
    def exitFuncDef(self, ctx:calculusparser.FuncDefContext):
        pass


    # Enter a parse tree produced by calculusparser#limitStmt.
    def enterLimitStmt(self, ctx:calculusparser.LimitStmtContext):
        pass

    # Exit a parse tree produced by calculusparser#limitStmt.
    def exitLimitStmt(self, ctx:calculusparser.LimitStmtContext):
        pass



del calculusparser