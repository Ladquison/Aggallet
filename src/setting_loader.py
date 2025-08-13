from ruamel.yaml import YAML
from ruamel.yaml.comments import CommentedMap
from yaml_loader_base import YamlLoaderBase

# load setting.yaml
class SettingLoader(YamlLoaderBase):
    # constructor
    def __init__(self, yaml: YAML, callback_enable: bool):
        super().__init__(yaml)
        self.callback_enable = callback_enable
    
    # validate setting.yaml
    def validate(self, data: CommentedMap) -> tuple[bool, str]:
        missing_key_list: list[str] = []

        required_top_key_list: list[str] = [
            "module_name_wasm",
            "wasm_ext",
            "type",
            "callback",
            "impl_wasm",
            "impl_ts",
        ]
        self.check_key_existence(data, required_top_key_list
                                 , "", missing_key_list)
        
        if "type" in data:
            type_data = data.get("type")
            required_key_list = [
                "catalog",
                "wasm",
                "ts",
            ]
            self.check_key_existence(type_data, required_key_list
                                     , "type.", missing_key_list)
        
        # all fields are ignored if callback is disabled
        if self.callback_enable:
            if not "callback" in data:
                missing_key_list.append("callback")
            else:
                callback_data = data.get("callback")
                required_key_list = [
                    "file_name",
                    "template_wasm",
                    "template_ts",
                    "enum_name",
                    "mapping_variable_name",
                    "function_name_add",
                    "function_name_remove",
                ]
                self.check_key_existence(callback_data, required_key_list
                                            , "callback.", missing_key_list)

        if "impl_wasm" in data:
            impl_wasm_data = data.get("impl_wasm")
            required_key_list = [
                "name",
                "template",
                "import_module",
                "call_prefix",
                "binding_name",
            ]
            self.check_key_existence(impl_wasm_data, required_key_list
                                     , "impl_wasm.", missing_key_list)

        if "impl_ts" in data:
            impl_ts_data = data.get("impl_ts")
            required_key_list = [
                "name",
                "template_wrapper",
                "template_type_def",
                "wasm_directory",
                "wasm_js_directory",
                "type_def_directory",
            ]
            self.check_key_existence(impl_ts_data, required_key_list
                                     , "impl_ts.", missing_key_list)
            
        message = ""
        result = len(missing_key_list) == 0
        if not result:
            message = f'Some keys are missing: {", ".join(missing_key_list)}'
        return result, message
