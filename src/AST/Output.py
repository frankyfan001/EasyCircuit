from AST.Node import Node


# AST for output
class Output(Node):

    def __init__(self, res, source):
        self.res = res
        self.source = source

    def accept(self, visitor):
        return visitor.visit_output(self)
