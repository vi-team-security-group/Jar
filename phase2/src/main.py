from lexer import tokenize
from parser import Parser
from interpreter import Interpreter

with open("examples/hello.jar", "r", encoding="utf-8") as f:
    code = f.read()

tokens = tokenize(code)
parser = Parser(tokens)
ast = parser.parse()
interpreter = Interpreter(ast)
for line in interpreter.run():
    print(line)
