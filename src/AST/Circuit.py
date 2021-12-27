from AST.Component import Component


# AST for Circuit
class Circuit(Component):
    def __init__(self, name, comp_type, components, connects, source):
        super().__init__(name, comp_type, source)
        self.components = components
        self.connects = connects

    def accept(self, visitor):
        return visitor.visit_circuit(self)

    # override to generate a deep copy of component object
    def __deepcopy__(self, memodict={}):
        return Circuit(self.name, self.type, self.components, self.connects, self.source)
