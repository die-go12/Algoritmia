from antlr4 import FileStream, CommonTokenStream
from .AlgoritmiaLexer import AlgoritmiaLexer
from .AlgoritmiaParser import AlgoritmiaParser
from .Executor import AlgoritmiaExecutor

def main():
    import sys

    if len(sys.argv) < 2:
        print("Debes indicar un archivo .alg")
        return

    archivo = sys.argv[1]

    # Leer archivo de entrada
    stream = FileStream(archivo, encoding="utf8")
    lexer = AlgoritmiaLexer(stream)
    tokens = CommonTokenStream(lexer)
    parser = AlgoritmiaParser(tokens)

    # Construir árbol
    tree = parser.programa()

    # Ejecutar visitor
    executor = AlgoritmiaExecutor()
    executor.visit(tree)

if __name__ == "__main__":
    main()
