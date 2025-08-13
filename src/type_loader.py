from pathlib import Path
from typing import Literal
from ruamel.yaml import YAML
from ruamel.yaml.comments import CommentedMap
from yaml_loader_base import YamlLoaderBase

# type information
class TypeInfo:
    def __init__(self, default: any):
        self.default = default

# load type information
class TypeLoader(YamlLoaderBase):
    # constructor
    def __init__(self, yaml: YAML):
        super().__init__(yaml)
        self.type_info_map: dict[str, TypeInfo] = {}
        self.ts_data = CommentedMap()
        self.wasm_data = CommentedMap()

    # validate type information
    def validate(self, data: CommentedMap) -> tuple[bool, str]:
        if not "types" in data:
            return False, "types does not exist"

        type_list = data.get("types")
        if not isinstance(type_list, list):
            return False, "types is not list"
        
        invalid_list: list[str] = []
        for info in type_list:
            if not "name" in info:
                invalid_list.append(f'invalid info is contained: {info}')
                continue
            is_success: bool = True
            if not "default" in info:
                is_success = False
                invalid_list.append(f'{info.get("name")} does not have default')
            if is_success:
                self.type_info_map[info.get("name")] = TypeInfo(info.get("default"))
        if len(invalid_list) != 0:
            return False, f'type list is invalid: {", ".join(invalid_list)}'

        return True, ""

    # load mapping information for type name
    # ex. int in YAML -> number in TypeScript
    def load_mapping_info(self, target: Literal["wasm", "ts"], path: Path) -> tuple[bool, str]:
        class MappingLoader(YamlLoaderBase):
            def __init__(inner_self, yaml: YAML):
                super().__init__(yaml)
            
            def validate(inner_self, data: CommentedMap) -> tuple[bool, str]:
                missing_type_list: list[str] = []
                for name in self.type_info_map.keys():
                    if not name in data:
                        missing_type_list.append(name)
                if len(missing_type_list) == 0:
                    return True, ""
                else:
                    return False, f'Some types are missing: {", ".join(missing_type_list)}'
        
        if target not in ("wasm", "ts"):
            raise ValueError('target must be "wasm" or "ts"')
        
        loader = MappingLoader(self.yaml)
        result, message = loader.load(path)
        if result:
            if target == "wasm":
                self.wasm_data = loader.data
            elif target == "ts":
                self.ts_data = loader.data
        return result, message
    
    # get mapping information
    def get_mapping_info(self, target: Literal["wasm", "ts"]):
        if target not in ("wasm", "ts"):
            raise ValueError('target must be "wasm" or "ts"')
        data = None
        if target == "wasm":
            data = self.wasm_data
        elif target == "ts":
            data = self.ts_data
        return data
    
    # check whether type is supported
    def is_support(self, type: str) -> bool:
        return type in self.type_info_map
    
    # get default value of type
    def get_default(self, type: str):
        return self.type_info_map[type].default