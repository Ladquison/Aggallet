/*
 * This source code is automatically generated.  
 * To make changes, please update the YAML file and run the code generation tool.
 */

import WASM from 'wasm/WASM.js';
import { CallbackMap, FUNCTION_ID } from 'types/WasmCallbackId';

export class WasmWrapper {
    private mInstance: Awaited<ReturnType<typeof WASM>> | undefined = undefined;

    /*
     * @brief load WebAssembly
     * @return promise for loading WebAssembly
     */
    public load(): Promise<void> {
        if (this.mInstance) {
            return Promise.resolve();
        }
        return WASM({
            locateFile: (fileName: string) => {
                if (fileName.endsWith('.wasm')) {
                    return `/wasm/${fileName}`;
                }
                return fileName;
            }
        }).then((result) => {
            this.mInstance = result;
        });
    }

    /*
     * @brief add callback function
     * @param id callback ID
     * @param func callback function
     * @return true: success, false: fail
     */
    public addCallback<ID extends keyof CallbackMap>(id: ID, func: CallbackMap[ID]): boolean {
        let result: boolean = false;
        if (this.mInstance) {
            result = this.mInstance.addCallback(id, func);
        }
        return result;
    }

    /*
     * @brief remove callback function
     * @param id callback ID
     * @return true: success, false: fail
     */
    public removeCallback(id: typeof FUNCTION_ID[keyof typeof FUNCTION_ID]): boolean {
        let result: boolean = false;
        if (this.mInstance) {
            result = this.mInstance.removeCallback(id);
        }
        return result;
    }

    /*
     * @brief periodic update
     */
    public update(
        ): void {
        if (this.mInstance) {
            this.mInstance.update(
                );
        }
        
    }

    /*
     * @brief bool test
     * @param arg1 argument 1
     * @return return bool
     */
    public test_bool(
        arg1: boolean): boolean {
        let result: boolean = false;
        if (this.mInstance) {
            result = this.mInstance.test_bool(
                arg1);
        }
        return result;
        
    }

    /*
     * @brief int float test
     * @param arg_int argument int
     * @param arg_float argument float
     * @return return float
     */
    public test_int_float(
        arg_int: number, arg_float: number): number {
        let result: number = 0;
        if (this.mInstance) {
            result = this.mInstance.test_int_float(
                arg_int, arg_float);
        }
        return result;
        
    }

    /*
     * @brief bool int string test
     * @param arg_1_bool argument 1 bool
     * @param arg_2_int argument 2 int
     * @param arg_3_string argument 3 string
     * @return return string
     */
    public test_bool_int_string(
        arg_1_bool: boolean, arg_2_int: number, arg_3_string: string): string {
        let result: string = "";
        if (this.mInstance) {
            result = this.mInstance.test_bool_int_string(
                arg_1_bool, arg_2_int, arg_3_string);
        }
        return result;
        
    }

    
}