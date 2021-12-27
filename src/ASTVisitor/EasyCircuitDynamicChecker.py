from common.common import get_pos_str


# Static class for dynamic checking
# called in Evaluator to perform check while evaluation is going
class EasyCircuitDynamicChecker:

    @staticmethod
    def checkUseVarBeforeDefined(var, vars_table, node):
        if var not in vars_table:
            raise Exception(f"At {get_pos_str(node)}  "
                            f"{var} is not defined before use!")

    @staticmethod
    def checkAlreadyDefinedVar(var, vars_table, node):
        if var in vars_table:
            raise Exception(f"At {get_pos_str(node)}  "
                            f"{var} is already defined!")

    @staticmethod
    def checkParamsArgsNumMismatch(num_args, num_params, node):
        if num_args != num_params:
            raise Exception(f"At {get_pos_str(node)}  "
                            f"the number of arguments [{num_args}] in {str(node)} mismatches "
                            f"the number of inputs [{num_params}] in circuit!")
