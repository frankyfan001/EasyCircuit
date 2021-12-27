from enum import Enum, auto


# Abstraction on component type
class ComponentTypeEnum(Enum):
    INPUT = auto()
    OUTPUT = auto()
    OR = auto()
    AND = auto()
    XOR = auto()
    CIRCUIT = auto()


# Abstraction for component type
# validation can be performed based on info stored in type
# For example, each component type should only accept certain number of input/output
# raise exception if user give wrong number of input/output
class ComponentType:
    input = 0
    output = 0
    type_enum: ComponentTypeEnum = None

    def __init__(self, type_enum, comp_input, comp_output):
        self.type_enum = type_enum
        self.input = comp_input
        self.output = comp_output

    def get_type_enum(self):
        return self.type_enum

    def get_input_output(self):
        return self.input, self.output

    # TODO: This should be part of validator, might want to remove it
    def check_input_output(self, give_input, give_output):
        if not give_input <= self.input or not give_output <= self.output:
            raise Exception(f"{self} can only accept {self.input} inputs and {self.output} outputs")
