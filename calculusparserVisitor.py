# Generated from calculusparser.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .calculusparser import calculusparser
else:
    from calculusparser import calculusparser

# This class defines a complete generic visitor for a parse tree produced by calculusparser.

class calculusparserVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by calculusparser#prog.
    def visitProg(self, ctx:calculusparser.ProgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by calculusparser#stat.
    def visitStat(self, ctx:calculusparser.StatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by calculusparser#expr.
    def visitExpr(self, ctx:calculusparser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by calculusparser#term.
    def visitTerm(self, ctx:calculusparser.TermContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by calculusparser#factor.
    def visitFactor(self, ctx:calculusparser.FactorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by calculusparser#atom.
    def visitAtom(self, ctx:calculusparser.AtomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by calculusparser#integralStmt.
    def visitIntegralStmt(self, ctx:calculusparser.IntegralStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by calculusparser#differentialEq.
    def visitDifferentialEq(self, ctx:calculusparser.DifferentialEqContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by calculusparser#partialEq.
    def visitPartialEq(self, ctx:calculusparser.PartialEqContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by calculusparser#initCond.
    def visitInitCond(self, ctx:calculusparser.InitCondContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by calculusparser#funcDef.
    def visitFuncDef(self, ctx:calculusparser.FuncDefContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by calculusparser#limitStmt.
    def visitLimitStmt(self, ctx:calculusparser.LimitStmtContext):
        return self.visitChildren(ctx)



del calculusparser