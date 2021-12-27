from AST.Node import Node


# AST for conditional statement
class IfThenElse(Node):
    def __init__(self, cond, then_statements, else_statements, source):
        super().__init__()
        self.cond = cond
        self.then_statements = then_statements
        self.else_statements = else_statements
        self.source = source

    def accept(self, visitor):
        return visitor.visit_ifThenElse(self)
