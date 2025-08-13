/*
 * This source code is automatically generated.  
 * To make changes, please update the YAML file and run the code generation tool.
 */

export const FUNCTION_ID = {
    
    /*
     * @brief respond parametes sent from TypeScript side
     * @param onoff toggle on/off
     * @param value numeric value multiplied by 10 and casted to integer
     * @param time string with two current times sent from TypeScript side
     */
    RESPOND_PARAMETERS: 0x0001,
    
} as const;

export type CallbackMap = {
    [FUNCTION_ID.RESPOND_PARAMETERS]: (onoff: boolean, value: number, time: string) => void;
    
};