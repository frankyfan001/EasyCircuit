from AST.Node import Node


# AST for a simulation
class Simulate(Node):
    def __init__(self, circuit_id, args, source):
        super().__init__()
        self.circuit_id = circuit_id
        self.args = args
        self.source = source

    def accept(self, visitor):
        return visitor.visit_simulate(self)

    def __str__(self):
        res = f"{self.circuit_id}("
        for i in range(len(self.args)):
            if not i == len(self.args) - 1:
                res += f"{str(self.args[i])}, "
            else:
                res += f"{str(self.args[i])}"
        res += ")"
        return res
