from typing import Callable
from ruamel.yaml import YAML
from ruamel.yaml.comments import CommentedMap
from yaml_loader_base import YamlLoaderBase

# value information
class ValueInfo:
    def __init__(self):
        self.comment = ""
        self.name = ""
        self.type = ""

# function information
class FunctionInfo:
    def __init__(self):
        self.id = 0
        self.comment = ""
        self.name = ""
        self.args = list[ValueInfo]()
        self.return_info = ValueInfo()

# load specification for functions
# comments in YAML are loaded and required to be listed next to fields "name" and "return"
class SpecLoader(YamlLoaderBase):
    # constructor
    def __init__(self, yaml: YAML, check_type: Callable[[str], bool]):
        super().__init__(yaml)
        self.function_list = list[FunctionInfo]()
        self.check_type = check_type

    # validate specification
    def validate(self, data: CommentedMap) -> tuple[bool, str]:
        if not "functions" in data:
            return False, "functions does not exist"
        
        functions_data = data.get("functions")
        if not isinstance(functions_data, list):
            return False, "functions is not list"
        
        invalid_list: list[str] = []
        for info in functions_data:
            if not "name" in info:
                invalid_list.append(f'invalid function is contained: {info}')
                continue
            
            func = FunctionInfo()
            func.name = info.get("name")
            func.comment = self.get_comment(info, "name")

            if not "return" in info:
                invalid_list.append(f'{func.name} does not have return')
                continue

            # in YAML, "return" information has only type
            return_type = info.get("return")
            if not self.check_type(return_type):
                invalid_list.append(f'return type of {func.name} is not supported: {return_type}')
                continue
            func.return_info.type = return_type
            func.return_info.comment = self.get_comment(info, "return")

            is_args_ok: bool = True
            if "args" in info:
                args = info.get("args")
                if not isinstance(args, list):
                    invalid_list.append(f'args of {func.name} is not list')
                    continue
                
                for arg in args:
                    if not "name" in arg:
                        is_args_ok = False
                        invalid_list.append(f'{func.name} contains invalid argument: {arg}')
                        continue
                    value = ValueInfo()
                    value.name = arg.get("name")
                    value.comment = self.get_comment(arg, "name")
                    if not "type" in arg:
                        invalid_list.append(f'{func.name} arg {value.name} does not have type')
                        continue
                    value.type = arg.get("type")
                    if not self.check_type(value.type):
                        invalid_list.append(f'{func.name} arg {value.name} is not supported: {value.type}')
                        continue
                    func.args.append(value)
                
            if is_args_ok:
                self.function_list.append(func)

        if len(invalid_list) != 0:
            return False, f'function list is invalid: {", ".join(invalid_list)}'
        
        return True, ""
    