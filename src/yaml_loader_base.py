from abc import ABC, abstractmethod
from pathlib import Path
from ruamel.yaml import YAML
from ruamel.yaml.comments import CommentedMap, CommentedSeq

# base class for loading YAML file
class YamlLoaderBase(ABC):
    # constructor
    def __init__(self, yaml: YAML):
        self.yaml = yaml
        self.data = CommentedMap()

    # load YAML file with path
    def load(self, path: Path) -> tuple[bool, str]:
        return self.load_with_data(path, self.data)

    # load YAML file with path and set to data passed as an argument
    def load_with_data(self, path: Path, data: CommentedMap) -> tuple[bool, str]:
        if not path.exists():
            return False, f'{path} does not exist'
        
        try:
            with path.open("r", encoding="utf-8") as f:
                data.update(self.yaml.load(f))
        except Exception as e:
            return False, f'Failed to load {path}: {e}'
        
        # validate YAML data
        is_success, message = self.validate(data)
        if is_success:
            return True, f'{path} was loaded successfully'
        else:
            return False, f'Failed to load {path}: {message}'
        
    # check whether required keys are contained in YAML data
    @staticmethod
    def check_key_existence(data: CommentedMap, required_key_list: list[str]
                            , missing_prefix: str, missing_key_list: list[str]):
        for key in required_key_list:
            if not key in data:
                missing_key_list.append(f'{missing_prefix}{key}')
    
    # validate YAML data
    @abstractmethod
    def validate(self, data: CommentedMap) -> tuple[bool, str]:
        pass

    # get YAML value with key
    def get(self, key: str):
        return self.data.get(key)
    
    # get comment in YAML
    def get_comment(self, node, key):
        result: str = ""
        if isinstance(node, CommentedMap):
            token = node.ca.items.get(key)
            if token and 2 < len(token) and token[2]:
                result = token[2].value.strip("# ").strip()
        return result
