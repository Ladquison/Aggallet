#pragma once

#include <map>
#include <emscripten/bind.h>
#include "Parameters.h"
#include "WasmCallbackId.h"

class CallbackUtility {
private:
    // added functions
    static std::map<FUNCTION_ID, emscripten::val> mFunctionMap;

public:
    // add callback function
    static bool addFunction(FUNCTION_ID ID, emscripten::val func);

    // remove callback function
    static bool removeFunction(FUNCTION_ID ID);

    // call callback function
    static void call(FUNCTION_ID ID, const Parameters& parameters);

private:
    // constructor
    CallbackUtility();

    // destructor
    virtual ~CallbackUtility();
};