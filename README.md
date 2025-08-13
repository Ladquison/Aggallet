# What is Armoron?

Armoron is a tool that automatically generates WebAssembly-related source code from function specifications defined in YAML files.  
The name is a combination of "Armor" and "Iron", inspired by my favorite game character.

---

# Overview

 - Function specifications must be defined in YAML.
 - Armoron reads the YAML and generates TypeScript code and source code for the WebAssembly implementation language.
 - Regarding the WebAssembly language, currently only support C++ by building with Emscripten.
 - Armoron generates interface code based on the specifications; business logic must be implemented by the user.
 
 ---

# Feature

Simply write specifications of functions you want to expose in WebAssembly in YAML format as shown below, and WebAssembly-related code will be generated automatically.
```yaml
functions:
  - name: update # periodic update
    return: void

  - name: test_bool # bool test
    args:
      - name: arg1 # argument 1
        type: bool
    return: bool # return bool
```
The generated code does the following:
 - Wrappers for invoking WebAssembly functions in TypeScript
 - Type definitions for WebAssembly function signatures in TypeScript
 - Bridging logic to expose public interfaces from the WebAssembly module in the WebAssembly-side language
 - Callback registration system, defining unique IDs for registering, unregistering, and invoking callbacks (implemented in both TypeScript and the WebAssembly-side language
)
 - Type definitions for callback functions in TypeScript

Comments written in the YAML file are reflected in the generated source code, with some limitations.

---

# Build Environment

Tested and confirmed in the following environment:
 - OS : Windows 11
 - Python : 3.9.13
 - Python library
   - Jinja2 : 3.1.6
   - ruamel.yaml : 0.18.14

---

# How to Use

1. Update `src/setting.yaml` as needed. This file describes the following settings. For individual settings, refer to the comments in the YAML file.
   - WebAssembly module name
   - Implementation language for WebAssembly
   - Variable names, class names, prefix of function names
   - Path to generated files or wasm file
   - Path to the YAML file that describes type information

2. In the following explanation, I will leave the YAML file that describes type information as the default.

3. Change the contents of `src/type/catalog.yaml` to match the type you want to use. Currently supported types are as follows, but they can easily be changed:
   - void
   - bool
   - int
   - float
   - string
   - function

4. Update the other files in `src/type` to define how each type is represented in the target language.
   - For example, in `src/type/ts.yaml`, "int" is mapped to "number".

5. Create a folder to store your function specification YAML files, and create `api.yaml`.

6. Write your function specifications in `api.yaml` as shown below:
```yaml
functions:
  - name: update # periodic update
    return: void

  - name: test_bool # bool test
    args:
      - name: arg1 # argument 1
        type: bool
    return: bool # return bool
```
   - name: Required. Function name. Comments on this line are reflected in the source code.
   - return: Required. Return type. Must be listed in `catalog.yaml`. Comments are reflected.
   - args: Optional. If present, specify name/type pairs in list format. Comments on each name are reflected.

7. To use callbacks, create `callback.yaml` in the same folder and write specifications in the same format as `api.yaml`.

8. Run src/armoron.py with the following arguments:
   - `-o`, `--output` : Path to the folder where generated files will be saved
   - `-s`, `--spec` : Path to the folder containing `api.yaml` and `callback.yaml`
   - `-c` : Optional. Required if using callbacks.

9. Generated source files will be saved to the specified output folder. Debug output is available in `src/debug/output` for reference.

---

# Example

Practical usage examples are available in the [`example`](./example).  
These demonstrate how to integrate Armoron with TypeScript and WebAssembly modules.

---

# License

This project is licensed under the [Apache License 2.0](https://www.apache.org/licenses/LICENSE-2.0).  
You are free to use, modify, and distribute this software for personal or commercial purposes,  
as long as you include the original license and copyright notice.

See the [LICENSE](./LICENSE) file for full details.
