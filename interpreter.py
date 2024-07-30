
from antlr4 import *
from KilianCode303va1Lexer import KilianCode303va1Lexer
from KilianCode303va1Parser import KilianCode303va1Parser
from KilianCode303va1Visitor import KilianCode303va1Visitor

class KilianCode303va1Interpreter(KilianCode303va1Visitor):
    def __init__(self):
        self.variables = {}
        self.functions = {}

    def visitProgram(self, ctx):
        for function in ctx.functionDefinition():
            self.visitFunctionDefinition(function)

    def visitFunctionDefinition(self, ctx):
        function_name = ctx.IDENTIFIER().getText()
        self.functions[function_name] = ctx.statement()

    def visitAssignment(self, ctx):
        var_name = ctx.IDENTIFIER().getText()
        value = self.visit(ctx.expression())
        self.variables[var_name] = value

    def visitConditionalStatement(self, ctx):
        condition = self.visit(ctx.expression())
        if condition:
            self.visit(ctx.statement(0))
        elif ctx.statement(1):
            self.visit(ctx.statement(1))

    def visitLoopingConstruct(self, ctx):
        if ctx.getChild(0).getText() == 'while':
            while self.visit(ctx.expression()):
                self.visit(ctx.statement())
        elif ctx.getChild(0).getText() == 'for':
            var_name = ctx.IDENTIFIER().getText()
            values = self.visit(ctx.expression())
            for value in values:
                self.variables[var_name] = value
                self.visit(ctx.statement())

    def visitFunctionCall(self, ctx):
        function_name = ctx.IDENTIFIER().getText()
        if function_name in self.functions:
            self.visit(self.functions[function_name])

    def visitReturnStatement(self, ctx):
        return self.visit(ctx.expression())

    def visitExpression(self, ctx):
        if ctx.STRING():
            return ctx.STRING().getText().strip('"')
        elif ctx.NUMBER():
            return int(ctx.NUMBER().getText())
        elif ctx.IDENTIFIER():
            return self.variables.get(ctx.IDENTIFIER().getText(), None)
        elif ctx.getChild(1).getText() == '+':
            return self.visit(ctx.expression(0)) + self.visit(ctx.expression(1))
        elif ctx.getChild(1).getText() == '-':
            return self.visit(ctx.expression(0)) - self.visit(ctx.expression(1))
        elif ctx.getChild(1).getText() == '*':
            return self.visit(ctx.expression(0)) * self.visit(ctx.expression(1))
        elif ctx.getChild(1).getText() == '/':
            return self.visit(ctx.expression(0)) / self.visit(ctx.expression(1))
        elif ctx.getChild(1).getText() == '%':
            return self.visit(ctx.expression(0)) % self.visit(ctx.expression(1))
        elif ctx.getChild(1).getText() == '§lo§':
            return self.visit(ctx.expression(0)) < self.visit(ctx.expression(1))
        elif ctx.getChild(1).getText() == '==':
            return self.visit(ctx.expression(0)) == self.visit(ctx.expression(1))

def main(filename):
    input_stream = FileStream(filename)
    lexer = KilianCode303va1Lexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = KilianCode303va1Parser(stream)
    tree = parser.program()
    interpreter = KilianCode303va1Interpreter()
    interpreter.visit(tree)

if __name__ == '__main__':
    import sys
    main(sys.argv[1])
