import os
import subprocess
import shutil

# Define the project directory
project_dir = os.path.join(os.path.expanduser("~"), "Desktop", "code_projects", "kc303va1_programming_language")

# Create the project directory
os.makedirs(project_dir, exist_ok=True)

# Define the grammar file content
grammar_content = """
grammar KilianCode303va1;

program: functionDefinition* EOF;

functionDefinition: '§§f§' IDENTIFIER statement*;

statement: assignment
         | conditionalStatement
         | loopingConstruct
         | functionCall
         | returnStatement;

assignment: IDENTIFIER '=' expression;

conditionalStatement: 'if' expression statement ('else' statement)?;

loopingConstruct: 'while' expression statement
                | 'for' IDENTIFIER 'in' expression statement;

functionCall: '§f§' IDENTIFIER;

returnStatement: 'return' expression;

expression: IDENTIFIER ('+' | '-' | '*' | '/' | '%' | '§lo§' | '==') IDENTIFIER
          | IDENTIFIER
          | STRING
          | NUMBER;

IDENTIFIER: '§xi§' NAME
          | '§xo§' NAME
          | '§v§' NAME
          | NAME;

NAME: [a-zA-Z_][a-zA-Z0-9_]*;

STRING: '"' .*? '"';

NUMBER: [0-9]+;

COMMENT: '/*' .*? '*/' -> skip;

WS: [ \\t\\r\\n]+ -> skip;
"""

# Define the interpreter file content
interpreter_content = """
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
"""

# Define the example file content
example_content = """
§§f§main
§xo§BACKUP_FOLDER = "autominibackups"
§xo§CONFIG_FILE = "autominibackups_file_watch_config.txt"

mkdir -p §xo§BACKUP_FOLDER

if [ ! -f §xo§CONFIG_FILE ]; then
echo "# Enter files to watch (one per line):" > §xo§CONFIG_FILE
echo "# Example: /path/to/file1.txt" >> §xo§CONFIG_FILE
echo " >> §xo§CONFIG_FILE"
echo "# LEAVE THIS AS THE LAST LINE PLEASE" >> §xo§CONFIG_FILE
echo "Config file created. Please add files to watch in §xo§CONFIG_FILE and run the script again."
exit 0
fi

if ! command -v entr &> /dev/null; then
echo "entr is not installed. Please install it and run the script again."
exit 1
fi

§§f§is_file_readable
§xi§file = §xi§1
if [ ! -f §xi§file ]; then
echo "Warning: File '§xi§file' does not exist. Skipping."
return 1
elif [ ! -r §xi§file ]; then
echo "Warning: File '§xi§file' is not readable. Skipping."
return 1
fi
return 0

§§f§watch_file
§xi§file = §xi§1
if §f§is_file_readable §xi§file; then
echo "Watching §xi§file"
filename="${§xi§file##*/}"
extension="${filename##*.}"
filename_no_ext="${filename%.*}"
timestamp=$(date +'%y%m%d%H%M%S')
backup_filename="${filename_no_ext}_autominibackup${timestamp}.${extension}"
echo §xi§file | entr -p sh -c "cp '§xi§file' '§xo§BACKUP_FOLDER/§xo§backup_filename'" &
fi

while IFS= read -r file; do
if [ -n §xi§file ] && [[ ! §xi§file =~ ^\s*# ]]; then
§f§watch_file §xi§file
fi
done < §xo§CONFIG_FILE

echo "File watching started. Press Ctrl+C to stop."
wait
"""

# Create the grammar file
grammar_file = os.path.join(project_dir, "KilianCode303va1.g4")
with open(grammar_file, "w") as f:
    f.write(grammar_content)

# Create the interpreter file
interpreter_file = os.path.join(project_dir, "interpreter.py")
with open(interpreter_file, "w") as f:
    f.write(interpreter_content)

# Create the example file
example_file = os.path.join(project_dir, "example.kc303va1")
with open(example_file, "w") as f:
    f.write(example_content)

# Install ANTLR
try:
    subprocess.run(["sudo", "apt-get", "install", "antlr4"], check=True)
except subprocess.CalledProcessError as e:
    print(f"Error installing ANTLR: {e}")
    exit(1)

# Install ANTLR Python runtime
try:
    subprocess.run(["pip", "install", "antlr4-python3-runtime"], check=True)
except subprocess.CalledProcessError as e:
    print(f"Error installing ANTLR Python runtime: {e}")
    exit(1)

# Generate the parser
try:
    subprocess.run(["antlr4", "-Dlanguage=Python3", "KilianCode303va1.g4"], cwd=project_dir, check=True)
except subprocess.CalledProcessError as e:
    print(f"Error generating the parser: {e}")
    exit(1)

print("Setup complete!")
