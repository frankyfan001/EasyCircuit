from AST.Node import Node


# AST for variable
class Var(Node):
    def __init__(self, identifier, source):
        super().__init__()
        self.identifier = identifier
        self.source = source

    def accept(self, visitor):
        return visitor.visit_var(self)

    def __str__(self):
        return self.identifier
