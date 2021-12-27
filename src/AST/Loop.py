from AST.Node import Node


# AST for loop
class Loop(Node):
    def __init__(self, inputs, statements, source):
        super().__init__()
        self.inputs = inputs
        self.statements = statements
        self.source = source

    def accept(self, visitor):
        return visitor.visit_loop(self)
