from AST.Node import Node


# AST for the entire program
class Program(Node):
    def __init__(self, statements):
        super().__init__()
        self.statements = statements

    def accept(self, visitor):
        return visitor.visit_program(self)
