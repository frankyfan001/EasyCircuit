import os

import antlr4
from antlr4 import CommonTokenStream

from parseTreeVisitor.EasyCircuitParseTreeToAST import EasyCircuitParseTreeVisitor
from src.ASTVisitor.EasyCircuitEvaluator import EasyCircuitEvaluator
from src.ASTVisitor.EasyCircuitStaticChecker import EasyCircuitStaticChecker
from src.parser.EasyCircuitLexer import EasyCircuitLexer
from src.parser.EasyCircuitParser import EasyCircuitParser


class ECEntry(object):

    @staticmethod
    def load(file_path):
        # User Input
        print(os.getcwd())
        f = open(file_path)
        user_input = antlr4.InputStream('\n'.join(f.readlines()))
        f.close()

        # Tokenization
        print('Starting Tokenization')
        lexer = EasyCircuitLexer(user_input)
        tokens = CommonTokenStream(lexer)

        # Parsing
        print('Starting Parsing')
        parser = EasyCircuitParser(tokens)
        parse_tree = parser.program()

        # AST Conversion
        print('Starting AST Conversion')
        parse_tree_to_ast = EasyCircuitParseTreeVisitor()
        ast = parse_tree_to_ast.visitProgram(parse_tree)

        # Static Checks
        print('Starting Static Checks')
        static_checker = EasyCircuitStaticChecker()
        ast.accept(static_checker)

        # Dynamic Checks & Evaluate
        print('Starting Dynamic Checks & Evaluate')
        evaluator = EasyCircuitEvaluator()
        ast.accept(evaluator)
