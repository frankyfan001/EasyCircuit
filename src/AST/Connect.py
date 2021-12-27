from src.AST.Node import Node


# AST for connect
class Connect(Node):
    def __init__(self, connect_from, connect_to, source):
        super().__init__()
        self.connect_from = connect_from
        self.connect_to = connect_to
        self.source = source

    def accept(self, visitor):
        return visitor.visit_connect(self)
