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
        update: (cycle: number) => void;
        setParameters: (onoff: boolean, value: number, time: string) => number;
        
    }>;
    export default WASM;
}