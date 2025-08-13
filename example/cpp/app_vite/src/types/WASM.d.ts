/*
 * This source code is automatically generated.  
 * To make changes, please update the YAML file and run the code generation tool.
 */

declare module 'wasm/WASM.js' {
    const WASM: (param: dict) => Promise<{
        addCallback: (id: number, func: Function) => boolean;
        removeCallback: (id: number) => boolean;
        update: (cycle: number) => void;
        setParameters: (onoff: boolean, value: number, time: string) => number;
        
    }>;
    export default WASM;
}