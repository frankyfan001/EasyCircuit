from AST.Circuit import Circuit
from AST.Component import Component
from AST.ComponentType import ComponentTypeEnum
from AST.Connect import Connect
from ASTVisitor.assets.GraphGenerator import GraphGenerator
from ASTVisitor.BaseASTVisitor import BaseASTVisitor
from toposort import toposort, CircularDependencyError

LOGIC_TYPE_MAPPING = {
    ComponentTypeEnum.INPUT: 'Dot',
    ComponentTypeEnum.OUTPUT: 'Dot',
    ComponentTypeEnum.AND: 'And',
    ComponentTypeEnum.OR: 'Or',
    ComponentTypeEnum.XOR: 'Xor'
}


# stub for code generator
class CodeGenerator(BaseASTVisitor):

    def __init__(self, circuit: Circuit):
        self.circuit = circuit
        self.gen_id = circuit.id
        graph_generator = GraphGenerator()
        self.var_name_map, graph = graph_generator.generate(circuit)
        # print(self.var_name_map)
        # print(graph)
        self.scheme = "from schemdraw import * \nd = schemdraw.Drawing(unit=.5)\n"

    def generate(self):
        self.visit_circuit(self.circuit)
        print(self.scheme)
        return self.scheme

    def visit_circuit(self, circuit: Circuit):
        for node in circuit.nodes:
            node.accept(self)

    def visit_component(self, component: Component):
        return self.generate_component_scheme(component)

    def generate_component_scheme(self, component: Component):
        # pass
        var_name = self.var_name_map[component.id]
        type_scheme = component.get_type_enum().name[0] + component.get_type_enum().name[1:].lower()
        if type_scheme == "Input" or type_scheme == "Output" or type_scheme == "Circuit":
            scheme = f"({var_name} := logic.Dot())"
        else:
            scheme = f"({var_name} := logic.{type_scheme}())"
        return scheme

    def visit_connect(self, connect: Connect):
        self.scheme += self.generate_connect_scheme(connect)

    def generate_connect_scheme(self, connect: Connect):
        from_comp = connect.connect_from
        to_comp = connect.connect_to
        from_name = self.var_name_map[from_comp.id]
        scheme = f"d += {self.visit_component(from_comp)}\n"
        scheme += f"d += logic.Line().right().at({from_name}.out).length(d.unit)\n"
        scheme += f"d += {self.visit_component(to_comp)}\n"
        return scheme


class SchemeGenerator(object):

    def __init__(self, circuit: Circuit):
        self.scheme = "import schemdraw\nfrom schemdraw import logic \nd = schemdraw.Drawing(unit=.5)\n"
        self.connects = {}
        self.name_map, self.graph = GraphGenerator().generate(circuit)
        self.drawed = []
        try:
            self.topoli = list(toposort(self.graph.copy()))
        except CircularDependencyError:
            raise CircularDependencyError

    def generate(self):
        inputs = self.topoli[-1]
        scheme = ""
        for input_comp in inputs:
            scheme += self.generate_input(input_comp)
        return self.scheme + scheme

    def generate_input(self, input_comp):
        name = self.name_map[input_comp.id]
        neighbors = self.graph[input_comp]
        self.drawed.append(name)
        scheme = ""
        scheme += f"d += ({name} := logic.Dot().label('{input_comp.name}', 'left'))\n"
        # scheme += f"d += logic.Line().left().label('{input_comp.name}', 'left')\n"
        for neighbor in neighbors:
            scheme += self.generate_connection(input_comp, neighbor)
        return scheme

    def generate_connection(self, from_comp, to_comp):
        print(f"from {from_comp.name} to {to_comp.name}")
        scheme = f"d += logic.Line().right()\n"
        from_name = self.name_map[from_comp.id]
        to_name = self.name_map[to_comp.id]
        if to_name not in self.connects:
            self.connects[to_name] = 0
        self.connects[to_name] += 1
        if to_name in self.drawed:
            scheme += f"d += logic.Line().at({to_name}.in{self.connects[to_name]})\n"
            if from_comp.get_type_enum() == ComponentTypeEnum.INPUT \
                    or from_comp.get_type_enum() == ComponentTypeEnum.OUTPUT:
                scheme += f"d += logic.Line().left().to({from_name}.start)"
            else:
                scheme += f"d += logic.Line().left().to({from_name}.out)"
        else:
            self.drawed.append(to_name)
            # if to_comp.get_type_enum() == ComponentTypeEnum.OUTPUT \
            #         or to_comp.get_type_enum() == ComponentTypeEnum.INPUT:
            #     type_scheme = "Dot"
            # else:
            #     type_scheme = to_comp.get_type_enum().name[0] + to_comp.get_type_enum().name[1:].lower()
            # scheme += f"d += ({to_name} := logic.{type_scheme}().anchor('in{self.connects[to_name]}'))\n"

            if from_comp.get_type_enum() == ComponentTypeEnum.INPUT \
                    or from_comp.get_type_enum() == ComponentTypeEnum.OUTPUT:
                scheme += f"d += logic.Line().right().at({from_name}.start)\n"
            else:
                scheme += f"d += logic.Line().right().at({from_name}.out)\n"
            if to_comp.get_type_enum() == ComponentTypeEnum.INPUT \
                    or to_comp.get_type_enum() == ComponentTypeEnum.OUTPUT:
                scheme += f"d += ({from_name} := logic.Dot())"
                scheme += f"d += logic.Line().right().at({from_name}.start)\n"
            else:
                scheme += f"d += logic.Line().right().at({from_name}.out)\n"
            scheme += f"d += logic.Line().to({to_name}.in{self.connects[to_name]})\n"

        if to_comp not in self.graph:
            return scheme

        neighbors = self.graph[to_comp]
        for neighbor in neighbors:
            scheme += self.generate_connection(to_comp, neighbor)

        return scheme



