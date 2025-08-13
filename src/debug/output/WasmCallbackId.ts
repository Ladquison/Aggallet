/*
 * This source code is automatically generated.  
 * To make changes, please update the YAML file and run the code generation tool.
 */

export const FUNCTION_ID = {
    
    /*
     * @brief callback sample call
     */
    CALL: 0x0001,
    
    /*
     * @brief callback sample send parameters
     * @param arg1 argument bool
     * @param arg2 argument int
     * @param arg3 argument string
     */
    SEND_PARAMETERS: 0x0002,
    
} as const;

export type CallbackMap = {
    [FUNCTION_ID.CALL]: () => void;
    [FUNCTION_ID.SEND_PARAMETERS]: (arg1: boolean, arg2: number, arg3: string) => void;
    
};