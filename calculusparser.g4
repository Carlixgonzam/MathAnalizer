parser grammar Calculusparser;
options {tokenVocab=calculuslexer;}
prog: stat+ EOF;

stat: expr SEMICO | integralStmt SEMICO | differentialEq SEMICO | initCond SEMICO | partialEq SEMICO
                | funcDef SEMICO | limitStmt SEMICO;
expr: expr SUMA term | expr RESTA term | term;
term: term MULTI factor | term DIV factor| factor;
factor: atom POTE factor | atom;
atom: NUMBER 
    | ID 
    | SIN LPAREN expr RPAREN
    | COS LPAREN expr RPAREN
    | TAN LPAREN expr RPAREN
    | COT LPAREN expr RPAREN
    | SEC LPAREN expr RPAREN
    | CSC LPAREN expr RPAREN
    | ARCSIN LPAREN expr RPAREN
    | ARCCOS LPAREN expr RPAREN
    | ARCTAN LPAREN expr RPAREN
    | LN LPAREN expr RPAREN
    | LOG LPAREN expr RPAREN
    | EXP LPAREN expr RPAREN
    | SQRT LPAREN expr RPAREN
    | ABS LPAREN expr RPAREN
    | LPAREN expr RPAREN;

integralStmt: INTEGRAL expr DIFERENCIAL ID;
differentialEq: DERIVADAPRIMA LPAREN ID RPAREN IGUAL expr
                | SEGUNDADERIVADA LPAREN ID RPAREN IGUAL expr
                | DDX LPAREN ID RPAREN expr;
partialEq: DERIVADAP ID DIV DERIVADAP ID IGUAL expr;
initCond: ID LPAREN expr RPAREN (COLON | BARRA) expr;
funcDef: ID LPAREN ID RPAREN IGUAL expr;
limitStmt: 'lim' LBRACE ID ARROW expr RBRACE expr;