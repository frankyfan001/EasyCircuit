import uuid


# Base AST Node, other ast extend it
class Node:

    def __init__(self):
        self.id = uuid.uuid4().hex

    def accept(self, visitor):
        pass
