INTEGRAL : '∫';
DERIVADAP: '∂'; //parcial
DIFERENCIAL: 'd';
DERIVADAPRIMA: '\'';
SEGUNDADERIVADA: 'd2';
DT: 'dt'; //diferencial de t
DX: 'dx'; 
DDX: 'ddx' //operador segunda derivada
SUMA: '+';
RESTA: '-';
MULTI: '*';
DIV: '/';
POTE: '^';
IGUAL: '=';
COLON: ':';
BARRA: '|';
LPAREN: '(';
RPAREN: ')';
LBRACE: '{';
RBRACE: '}';
LBRACK: '[';
RBRACK: ']';
COMA: ',';
SEMICO: ';';

SIN: 'sen';
COS: 'cos';
TAN: 'tan';
COT: 'cot';
SEC: 'sec';
CSC: 'csc';
ARCSIN: 'arcsen';
ARCCOS: 'arccos';
ARCTAN: 'arctan';
LN: 'ln';
LOG: 'log';
EXP: 'exp';
SQRT: 'sqrt';
ABS: 'abs';

PI: 'pi';
ECONST: 'e';
ARROW : '->';
DIGIT: [0-9];
NUMBER: DIGIT+ ('.' DIGIT+)? ([eE] [+-]? DIGIT+)?;
ID: [a-zA-Z_] [a-zA-Z_0-9]*
WS: [\t\r\n]+ -> skip;
COMENTARIO: '/*' .*? '*/' -> skip;
LINEACOMENT: '//' ~[\r\n]* -> skip;

expr: expr SUMA expr | NUMBER;