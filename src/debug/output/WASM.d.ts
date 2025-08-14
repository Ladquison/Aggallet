/*
 * This source code is automatically generated.  
 * To make changes, please update the YAML file and run the code generation tool.
 */

type WASMOptions = {
  locateFile?: (fileName: string) => string;
};

declare module 'wasm/WASM.js' {
    const WASM: (options: WASMOptions) => Promise<{
        addCallback: (id: number, func: Function) => boolean;
        removeCallback: (id: number) => boolean;
        update: () => void;
        test_bool: (arg1: boolean) => boolean;
        test_int_float: (arg_int: number, arg_float: number) => number;
        test_bool_int_string: (arg_1_bool: boolean, arg_2_int: number, arg_3_string: string) => string;
        
    }>;
    export default WASM;
}