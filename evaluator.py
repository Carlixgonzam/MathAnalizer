import sympy as sp
import numpy as np
import matplotlib.pyplot as plt
from antlr4 import CommonTokenStream, FileStream
from calculuslexer import calculuslexer
from calculusparser import calculusparser
from calculusparserVisitor import calculusparserVisitor

class EvalVisitor(calculusparserVisitor):
    def __init__(self):
        self.env = {}

# -------------------- programa --------------------
    def visitProg(self, ctx):
        results = []
        for stat in ctx.stat():
            res = self.visit(stat)
            results.append(res)
        return results

    def visitEvalExpr(self, ctx):
        # expr SEMICO
        return self.visit(ctx.expr())
    def visitAdd(self, ctx):
        return self.visit(ctx.expr()) + self.visit(ctx.term())
    def visitSubtract(self, ctx):
        return self.visit(ctx.expr()) - self.visit(ctx.term())
    def visitMultiply(self, ctx):
        return self.visit(ctx.term()) * self.visit(ctx.factor())
    def visitDivide(self, ctx):
        return self.visit(ctx.term()) / self.visit(ctx.factor())
    def visitPower(self, ctx):
        return self.visit(ctx.atom()) ** self.visit(ctx.factor())
    def visitNumber(self, ctx):
        text = ctx.getText()
        return sp.nsimplify(text)
    def visitVariable(self, ctx):
        name = ctx.getText()
        return self.env.get(name, sp.symbols(name))
    
    def visitFuncSin(self, ctx):   
        return sp.sin(self.visit(ctx.expr()))
    def visitFuncCos(self, ctx):   
        return sp.cos(self.visit(ctx.expr()))
    def visitFuncTan(self, ctx):   
        return sp.tan(self.visit(ctx.expr()))
    def visitFuncCot(self, ctx):   
        return 1/sp.tan(self.visit(ctx.expr()))
    def visitFuncSec(self, ctx):   
        return 1/sp.cos(self.visit(ctx.expr()))
    def visitFuncCsc(self, ctx):   
        return 1/sp.sin(self.visit(ctx.expr()))
    def visitFuncArcSin(self, ctx): 
        return sp.asin(self.visit(ctx.expr()))
    def visitFuncArcCos(self, ctx): 
        return sp.acos(self.visit(ctx.expr()))
    def visitFuncArcTan(self, ctx): 
        return sp.atan(self.visit(ctx.expr()))
    def visitFuncLn(self, ctx):    
        return sp.log(self.visit(ctx.expr()))
    def visitFuncLog(self, ctx):   
        return sp.log(self.visit(ctx.expr()), 10)
    def visitFuncExp(self, ctx):   
        return sp.exp(self.visit(ctx.expr()))
    def visitFuncSqrt(self, ctx):  
        return sp.sqrt(self.visit(ctx.expr()))
    def visitFuncAbs(self, ctx):   
        return sp.Abs(self.visit(ctx.expr()))
    def visitParens(self, ctx):    
        return self.visit(ctx.expr())

    def visitComputeIntegral(self, ctx):
        expr_sym = self.visit(ctx.expr())
        var = sp.symbols(ctx.ID().getText())
        result = sp.integrate(expr_sym, var)
        return result

    def visitFirstOrderEq(self, ctx):
        # y' = f(x)
        y_name = ctx.ID(0).getText()
        x = sp.symbols('x')
        f = self.visit(ctx.expr())
        y = sp.Function(y_name)
        ode = sp.Eq(sp.diff(y(x), x), f)
        sol = sp.dsolve(ode)
        return sol

    def visitSecondOrderEq(self, ctx):
        # y'' = f(x)
        y_name = ctx.ID(0).getText()
        x = sp.symbols('x')
        f = self.visit(ctx.expr())
        y = sp.Function(y_name)
        ode = sp.Eq(sp.diff(y(x), x, 2), f)
        sol = sp.dsolve(ode)
        return sol

    def visitOperatorSecondOrder(self, ctx):
        var_name = ctx.ID().getText()
        x = sp.symbols('x')
        y = sp.Function(var_name)
        return sp.diff(y(x), x, 2)

    def visitPartialEq(self, ctx):
        # ∂y/∂x = expr
        y = ctx.ID(0).getText()
        x = ctx.ID(1).getText()
        expr_sym = self.visit(ctx.expr())
        Y = sp.Function(y)
        X = sp.symbols(x)
        pde = sp.Eq(sp.diff(Y(X), X), expr_sym)
        sol = sp.dsolve(pde)
        return sol
    # -------------------- condicion inicial --------------------
    def visitInitCond(self, ctx):
        # y(x0)=y0
        name = ctx.ID().getText()
        x0 = self.visit(ctx.expr(0))
        y0 = self.visit(ctx.expr(1))
        return f"Condición inicial: {name}({x0}) = {y0}"
    # -------------------- definicion de funcion --------------------
    def visitFuncDef(self, ctx):
        fname = ctx.ID(0).getText()
        arg = sp.symbols(ctx.ID(1).getText())
        expr_sym = self.visit(ctx.expr())
        self.env[fname] = sp.Lambda(arg, expr_sym)
        return f"Función definida: {fname}({arg}) = {expr_sym}"

    # -------------------- limites --------------------
    def visitLimit(self, ctx):
        var = sp.symbols(ctx.ID().getText())
        to_value = self.visit(ctx.expr(0))
        expr_sym = self.visit(ctx.expr(1))
        limit_val = sp.limit(expr_sym, var, to_value)
        return limit_val

def parse_and_evaluate(file_path):
    input_stream = FileStream(file_path, encoding='utf-8')
    lexer = calculuslexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = calculusparser(stream)
    tree = parser.prog()
    visitor = EvalVisitor()
    return visitor.visit(tree)

if __name__ == '__main__':
    results = parse_and_evaluate('input.txt')
    for r in results:
        print(r)
