/*
 * This source code is automatically generated.  
 * To make changes, please update the YAML file and run the code generation tool.
 */

#pragma once

enum class FUNCTION_ID : uint16_t {

    /*
     * @brief respond parametes sent from TypeScript side
     * @param onoff bool value. toggle on/off
     * @param value int value. numeric value multiplied by 10 and casted to integer
     * @param time std::string value. string with two current times sent from TypeScript side
     */
    RESPOND_PARAMETERS = 0x0001,
};