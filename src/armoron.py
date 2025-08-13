import argparse
from pathlib import Path
import sys
from ruamel.yaml import YAML
from callback_id_manager import CallbackIdManager
from code_generator import CodeGenerator
from command_arg_manager import CommandArgManager
from setting_loader import SettingLoader
from spec_loader import SpecLoader
from type_loader import TypeLoader

parser = argparse.ArgumentParser(description="Source File Auto Generation Tool for WebAssembly")
parser.add_argument("-s", "--spec", required=True,
    help="directory where function specifications are located"
)
parser.add_argument("-o", "--output", required=True,
    help="directory where generated source files will be output"
)
parser.add_argument("-c", action="store_true",
    help="use callback"
)
args = parser.parse_args()

result: bool = False
message: str = ""

# check arguments
command_arg_manager = CommandArgManager(args)
result, message = command_arg_manager.check()
if not result:
    print(f'Arguments are invalid. Message is "{message}".')
    sys.exit()

# generate YAML instance, do not use safety loading for using comment in YAML
yaml = YAML()
script_dir = Path(__file__).parent.resolve()
callback_enable = command_arg_manager.is_callback_enable()

# load setting.yaml
setting_loader = SettingLoader(yaml, callback_enable)
result, message = setting_loader.load(script_dir / "setting.yaml")
if not result:
    print(f'Failed to load setting.yaml. Message is "{message}".')
    sys.exit()
print(f'Loaded setting.yaml successfully.')

# load type information
# information is written in "type" field in setting.yaml
type_loader = TypeLoader(yaml)

# load what type to use
result, message = type_loader.load(script_dir / setting_loader.get("type").get("catalog"))
if not result:
    print(f'Failed to load type catalog. Message is "{message}".')
    sys.exit()

# load converted type by used language
# ex. int in YAML -> number in TypeScript
result, message = type_loader.load_mapping_info("wasm"
    , script_dir / setting_loader.get("type").get("wasm"))
if not result:
    print(f'Failed to load WebAssembly type. Message is "{message}".')
    sys.exit()
result, message = type_loader.load_mapping_info("ts"
    , script_dir / setting_loader.get("type").get("ts"))
if not result:
    print(f'Failed to load TypeScript type. Message is "{message}".')
    sys.exit()
print(f'Loaded type information successfully.')

# load function information implemented by WebAssembly
def check_type(type: str) -> bool:
    return type_loader.is_support(type)
api_loader = SpecLoader(yaml, check_type)
result, message = api_loader.load(command_arg_manager.get_api_file_path())
if not result:
    print(f'Failed to load API spec. Message is "{message}".')
    sys.exit()

# load callback function information if callback is enabled
if callback_enable:
    callback_loader = SpecLoader(yaml, check_type)
    result, message = callback_loader.load(command_arg_manager.get_callback_file_path())
    if not result:
        print(f'Failed to load callback spec. Message is "{message}".')
        sys.exit()
    callback_id_manager = CallbackIdManager(
        command_arg_manager.get_spec_dir_path() / "callback_id_cache.json")
    callback_id_manager.set_function_id(callback_loader.function_list)
print(f'Loaded function specification successfully.')

# generate source code
code_generator = CodeGenerator(script_dir, args.output, callback_enable
                               , setting_loader, type_loader, api_loader)
code_generator.generate_wasm()
print(f'Generated WebAssembly source files.')
code_generator.generate_ts()
print(f'Generated TypeScript source files.')
if callback_enable:
    code_generator.set_callback_loader(callback_loader)
    code_generator.generate_callback()
    print(f'Generated callback source files.')
