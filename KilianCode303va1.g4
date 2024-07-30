
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

WS: [ \t\r\n]+ -> skip;
