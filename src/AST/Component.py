from antlr4 import Token

from AST.ComponentType import ComponentType
from AST.Node import Node


# AST for Component
class Component(Node):
    def __init__(self, name: str, comp_type: ComponentType, source: Token):
        super().__init__()
        self.type = comp_type  # e.g. AND, OR, INPUT, OUTPUT
        self.name = name
        self.inbound = []
        self.outbound = None
        self.scheme = None
        self.source = source

    def accept(self, visitor):
        return visitor.visit_component(self)

    def get_type_enum(self):
        return self.type.get_type_enum()

    def check_input_output(self, given_input, given_output):
        self.type.check_input_output(given_input, given_output)

    def get_input_output(self):
        return self.type.get_input_output()
