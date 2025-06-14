from antlr4 import FileStream, CommonTokenStream
from calculuslexer import calculuslexer
from calculusparser import calculusparser

def main():
    stream = FileStream("input.txt", encoding="utf-8")
    lexer  = calculuslexer(stream)
    tokens = CommonTokenStream(lexer)
    parser = calculusparser(tokens)
    tree   = parser.prog()        
    print(tree.toStringTree(recog=parser))
if __name__ == "__main__":
    main()