from AST.Node import Node


# AST for drawing
class Draw(Node):
    def __init__(self, name, simulate, source):
        super().__init__()
        self.name = name
        self.simulate = simulate
        self.source = source

    def accept(self, visitor):
        return visitor.visit_draw(self)
