from AST.Node import Node


# Number constant AST
class Num(Node):
    def __init__(self, value, source):
        super().__init__()
        self.value = value
        self.source = source

    def accept(self, visitor):
        return visitor.visit_num(self)

    def __str__(self):
        return self.value
