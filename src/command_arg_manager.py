import os
from pathlib import Path

class CommandArgManager:
    # constructor
    def __init__(self, args):
        self.args = args
        self.spec_dir_path = Path()
        self.api_file_path = Path()
        self.callback_enable = False
        self.callback_file_path = Path()
    
    # check arguments
    def check(self) -> tuple[bool, str]:
        # check whether callback is enabled
        self.callback_enable = self.args.c

        # check specification direcotry
        if not os.path.isabs(self.args.spec):
            return False, f'{self.args.spec} is not absolute path'
        if not os.path.isdir(self.args.spec):
            return False, f'{self.args.spec} is not directory'
        self.spec_dir_path = Path(self.args.spec)
        
        # check API file
        api_file = os.path.join(self.args.spec, "api.yaml")
        if not os.path.isfile(api_file):
            return False, f'api.yaml does not exist in {self.args.spec}'
        self.api_file_path = Path(api_file)

        # check callback file
        if self.callback_enable:
            callback_file = os.path.join(self.args.spec, "callback.yaml")
            if os.path.isfile(callback_file):
                self.callback_file_path = Path(callback_file)
            else:
                return False, f'callback.yaml does not exist in {self.args.spec}'
        
        # check output directory
        if not os.path.isabs(self.args.output):
            return False, f'{self.args.output} is not absolute path'
        if not os.path.isdir(self.args.output):
            return False, f'{self.args.output} is not directory'
        
        return True, ""
    
    # get directory path for specification
    def get_spec_dir_path(self) -> Path:
        return self.spec_dir_path
    
    # get file path for "api.yaml"
    def get_api_file_path(self) -> Path:
        return self.api_file_path
    
    # return whether callbais is enabled
    def is_callback_enable(self) -> Path:
        return self.callback_enable
    
    # get file path for "callback.yaml"
    def get_callback_file_path(self) -> Path:
        return self.callback_file_path