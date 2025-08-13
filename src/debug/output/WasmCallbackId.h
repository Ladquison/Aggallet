/*
 * This source code is automatically generated.  
 * To make changes, please update the YAML file and run the code generation tool.
 */

#pragma once

enum class FUNCTION_ID : uint16_t {

    /*
     * @brief callback sample call
     */
    CALL = 0x0001,

    /*
     * @brief callback sample send parameters
     * @param arg1 bool value. argument bool
     * @param arg2 int value. argument int
     * @param arg3 std::string value. argument string
     */
    SEND_PARAMETERS = 0x0002,
};