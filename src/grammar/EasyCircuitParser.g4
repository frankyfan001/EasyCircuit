parser grammar EasyCircuitParser;
options { tokenVocab = EasyCircuitLexer; }

program     : statement*;
statement   : circuit | component | connect | draw | simulate | output | ifthenelse | loop;
circuit     : CIRCUIT_START ID LEFT_BRACKET component* connect+ RIGHT_BRACKET;
component   : TYPE ID SEMICOLON | circuit;
connect     : ID ARROW ID SEMICOLON;

// Rule for draw
draw        : DRAW_START (ID | simulate) SEMICOLON;

// Rules for simulate
simulate    : ID LEFT_PAREN args RIGHT_PAREN SEMICOLON?;
args        : (exp COMMA)* exp;
exp         : num | var | simulate;
num         : NUM;
var         : ID;

// Rule for output
output      : OUTPUT_START simulate SEMICOLON;

// Rules for ifthenelse
ifthenelse: IF exp LEFT_BRACKET thenblock=statements RIGHT_BRACKET
            (ELSE LEFT_BRACKET elseblock=statements RIGHT_BRACKET)?;
statements: statement*;

// Rules for loop
loop        : LOOP_START LEFT_SQUARE_BRACKET inputs RIGHT_SQUARE_BRACKET LEFT_BRACKET statement* RIGHT_BRACKET;
inputs      : (ID COMMA)* ID;
