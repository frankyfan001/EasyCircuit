import abc

from src.AST.Program import Program
from src.AST.Circuit import Circuit
from src.AST.Component import Component
from src.AST.Connect import Connect
from src.AST.Draw import Draw
from src.AST.Simulate import Simulate
from src.AST.Num import Num
from src.AST.Var import Var
from src.AST.Output import Output
from src.AST.IfThenElse import IfThenElse
from src.AST.Loop import Loop


# abstract interface for AST visitor:
# https://stackoverflow.com/questions/13646245/is-it-possible-to-make-abstract-classes-in-python
class BaseASTVisitor(abc.ABC):
    @abc.abstractmethod
    def visit_program(self, program: Program):
        pass

    @abc.abstractmethod
    def visit_circuit(self, circuit: Circuit):
        pass

    @abc.abstractmethod
    def visit_component(self, component: Component):
        pass

    @abc.abstractmethod
    def visit_connect(self, connect: Connect):
        pass

    @abc.abstractmethod
    def visit_draw(self, draw: Draw):
        pass

    @abc.abstractmethod
    def visit_simulate(self, simulate: Simulate):
        pass

    @abc.abstractmethod
    def visit_num(self, num: Num):
        pass

    @abc.abstractmethod
    def visit_var(self, var: Var):
        pass

    @abc.abstractmethod
    def visit_output(self, output: Output):
        pass

    @abc.abstractmethod
    def visit_ifThenElse(self, if_then_else: IfThenElse):
        pass

    @abc.abstractmethod
    def visit_loop(self, loop: Loop):
        pass
