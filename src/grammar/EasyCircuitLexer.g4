lexer grammar EasyCircuitLexer;

CIRCUIT_START   : 'CIRCUIT ';
LEFT_BRACKET    : '{';
RIGHT_BRACKET   : '}';
LEFT_PAREN      : '(';
RIGHT_PAREN     : ')';
LEFT_SQUARE_BRACKET:'[';
RIGHT_SQUARE_BRACKET: ']';
SEMICOLON       : ';';
ARROW           : '->' | '=>';
COMMA           : ',';
EQ              : '=';
TYPE            : 'INPUT ' | 'OUTPUT ' | 'AND ' | 'OR ' | 'XOR ';
DRAW_START      : 'draw ';
OUTPUT_START    : 'output ';
IF              : 'if ';
ELSE            : 'else';
LOOP_START      : 'loop ';

NUM             : [0-9]+;
ID              : [a-zA-Z_] [a-zA-Z_0-9]*;

WS: [ \t\n\r] -> channel(HIDDEN);
