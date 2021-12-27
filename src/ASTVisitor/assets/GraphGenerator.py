from AST.ComponentType import ComponentTypeEnum
from ASTVisitor.BaseASTVisitor import BaseASTVisitor
from AST.Circuit import Circuit
from AST.Component import Component
from AST.Connect import Connect


class GraphGenerator(BaseASTVisitor):

    def __init__(self):
        self.graph = {}
        self.counter = {}
        self.var_name_mapping = {}
        self.circuit_io_mapping = {}

    def generate(self, circuit: Circuit):
        circuit_io_mapper = CircuitIOMapper(circuit)
        self.circuit_io_mapping = circuit_io_mapper.map_circuit_input_output()
        self.visit_circuit(circuit)
        return self.var_name_mapping, self.graph

    def visit_circuit(self, circuit: Circuit):
        type_enum = circuit.get_type_enum()
        if type_enum not in self.counter:
            self.counter[type_enum] = 0
        else:
            self.counter[type_enum] += 1
        var_name = str(type_enum.name) + str(self.counter[type_enum])
        self.var_name_mapping[circuit.id] = var_name
        for node in circuit.nodes:
            node.accept(self)

    def visit_component(self, component: Component):
        type_enum = component.get_type_enum()
        if type_enum not in self.counter:
            self.counter[type_enum] = 0
        else:
            self.counter[type_enum] += 1
        var_name = str(type_enum.name)[0] + str(self.counter[type_enum])
        self.var_name_mapping[component.id] = var_name

    def visit_connect(self, connect: Connect):
        # print("circuit io mapping: ")
        # print(self.circuit_io_mapping)
        from_comp: Component = connect.connect_from
        to_comp: Component = connect.connect_to
        # print(from_comp.get_type_enum())
        if from_comp.get_type_enum() == ComponentTypeEnum.CIRCUIT:
            if from_comp.id not in self.circuit_io_mapping or not self.circuit_io_mapping[from_comp.id]["input"]:
                raise Exception(f"Circuit {from_comp.name} does not have enough input")
            new_from_comp = self.circuit_io_mapping[from_comp.id]["output"][0]
            # print(f"from name: {from_comp.name} from type: {from_comp.get_type_enum()}")
            self.circuit_io_mapping[from_comp.id]["output"] = self.circuit_io_mapping[from_comp.id]["output"][1:]
            from_comp = new_from_comp

        if to_comp.get_type_enum() == ComponentTypeEnum.CIRCUIT:
            if to_comp.id not in self.circuit_io_mapping or not self.circuit_io_mapping[to_comp.id][1]:
                raise Exception(f"Circuit {from_comp.name} does not have enough input")
            # print(f"to name: {to_comp.name} to type: {to_comp.get_type_enum()}")
            new_to_comp = self.circuit_io_mapping[to_comp.id]["input"][0]
            self.circuit_io_mapping[to_comp.id]["input"] = self.circuit_io_mapping[to_comp.id]["input"][1:]
            to_comp = new_to_comp

        if connect.connect_from not in self.graph:
            self.graph[from_comp] = []
        self.graph[from_comp].append(to_comp)


class CircuitIOMapper(BaseASTVisitor):

    def __init__(self, circuit):
        self.circuit = circuit
        self.circuit_io_map = {}
        self.circuit_ids = []

    def map_circuit_input_output(self):
        self.visit_circuit(self.circuit)
        return self.circuit_io_map

    def visit_component(self, component: Component):
        if component.get_type_enum() == ComponentTypeEnum.INPUT:
            for cid in self.circuit_ids:
                self.circuit_io_map[cid]["input"].append(component)
        elif component.get_type_enum() == ComponentTypeEnum.OUTPUT:
            for cid in self.circuit_ids:
                self.circuit_io_map[cid]["output"].append(component)

    def visit_connect(self, connect: Connect):
        pass

    def visit_circuit(self, circuit: Circuit):
        self.circuit_ids.append(circuit.id)
        self.circuit_io_map[circuit.id] = {"input": [], "output": []}
        for node in circuit.nodes:
            node.accept(self)
        self.circuit_ids.pop()
