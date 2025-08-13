/*
 * This source code is automatically generated.  
 * To make changes, please update the YAML file and run the code generation tool.
 */

#include <emscripten/bind.h>
#include <emscripten/emscripten.h>

#include "AppWrapper.h"

/*
 * @brief add callback function
 * @param id callback ID
 * @param func callback function
 * @return true: success, false: fail
 */
bool addCallback(uint16_t id, emscripten::val func) {
    return AppWrapper::getInstance().addCallback(id, func);
}

/*
 * @brief remove callback function
 * @param id callback ID
 * @return true: success, false: fail
 */
bool removeCallback(uint16_t id) {
    return AppWrapper::getInstance().removeCallback(id);
}

/*
 * @brief periodic update
 * @param cycle execution cycle (millisecond)
 */
void update(
    int cycle) {
    AppWrapper::getInstance().update(
        cycle);
}

/*
 * @brief set parameters
 * @param onoff toggle on/off
 * @param value numeric value
 * @param time current time
 * @return number of calls
 */
int setParameters(
    bool onoff, float value, std::string time) {
    return AppWrapper::getInstance().setParameters(
        onoff, value, time);
}

EMSCRIPTEN_BINDINGS(bind_module) {
    emscripten::function("addCallback", &addCallback);
    emscripten::function("removeCallback", &removeCallback);
    emscripten::function("update", &update);
    emscripten::function("setParameters", &setParameters);
    }