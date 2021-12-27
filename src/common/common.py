from AST.ComponentType import ComponentTypeEnum

# A common map that map type str to its enum and input/output number
TYPECHECK_MAP = {"INPUT ": (ComponentTypeEnum.INPUT, 0, 1), "OUTPUT ": (ComponentTypeEnum.OUTPUT, 1, 0),
                 "AND ": (ComponentTypeEnum.AND, 2, 1), "OR ": (ComponentTypeEnum.OR, 2, 1),
                 "XOR ": (ComponentTypeEnum.XOR, 2, 1), "CIRCUIT ": (ComponentTypeEnum.CIRCUIT, 1, 1)}


# Helper function to get a ast node's position
def get_pos_str(node):
    assert node.source
    return f"line {(node.source.line + 1) // 2}:{node.source.column}"
