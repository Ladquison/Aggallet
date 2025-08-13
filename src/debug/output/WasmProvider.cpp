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
 */
void update(
    ) {
    AppWrapper::getInstance().update(
        );
}

/*
 * @brief bool test
 * @param arg1 argument 1
 * @return return bool
 */
bool test_bool(
    bool arg1) {
    return AppWrapper::getInstance().test_bool(
        arg1);
}

/*
 * @brief int float test
 * @param arg_int argument int
 * @param arg_float argument float
 * @return return float
 */
float test_int_float(
    int arg_int, float arg_float) {
    return AppWrapper::getInstance().test_int_float(
        arg_int, arg_float);
}

/*
 * @brief bool int string test
 * @param arg_1_bool argument 1 bool
 * @param arg_2_int argument 2 int
 * @param arg_3_string argument 3 string
 * @return return string
 */
std::string test_bool_int_string(
    bool arg_1_bool, int arg_2_int, std::string arg_3_string) {
    return AppWrapper::getInstance().test_bool_int_string(
        arg_1_bool, arg_2_int, arg_3_string);
}

EMSCRIPTEN_BINDINGS(bind_module) {
    emscripten::function("addCallback", &addCallback);
    emscripten::function("removeCallback", &removeCallback);
    emscripten::function("update", &update);
    emscripten::function("test_bool", &test_bool);
    emscripten::function("test_int_float", &test_int_float);
    emscripten::function("test_bool_int_string", &test_bool_int_string);
    }