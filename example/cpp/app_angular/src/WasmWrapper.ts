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
     * @param cycle execution cycle (millisecond)
     */
    public update(
        cycle: number): void {
        if (this.mInstance) {
            this.mInstance.update(
                cycle);
        }
        
    }

    /*
     * @brief set parameters
     * @param onoff toggle on/off
     * @param value numeric value
     * @param time current time
     * @return number of calls
     */
    public setParameters(
        onoff: boolean, value: number, time: string): number {
        let result: number = 0;
        if (this.mInstance) {
            result = this.mInstance.setParameters(
                onoff, value, time);
        }
        return result;
        
    }

    
}