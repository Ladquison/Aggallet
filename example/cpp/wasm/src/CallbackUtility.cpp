#include "CallbackUtility.h"

using namespace std;
using namespace emscripten;

map<FUNCTION_ID, val> CallbackUtility::mFunctionMap;

CallbackUtility::CallbackUtility() {
}

CallbackUtility::~CallbackUtility() {
}

bool CallbackUtility::addFunction(FUNCTION_ID ID, val func) {
    bool updated = false;
    if (mFunctionMap.count(ID) == 0) {
        mFunctionMap[ID] = func;
        updated = true;
    }
    return updated;
}

bool CallbackUtility::removeFunction(FUNCTION_ID ID) {
    bool updated = false;
    if (mFunctionMap.count(ID) != 0) {
        mFunctionMap.erase(ID);
        updated = true;
    }
    return updated;
}

void CallbackUtility::call(FUNCTION_ID ID, const Parameters& parameters) {
    if (mFunctionMap.count(ID) != 0) {
        const auto& parameterList = parameters.getParameterList();
        val args = val::array();
        for (size_t index = 0; index < parameterList.size(); ++index) {
            const auto& value = parameterList[index];
            switch (value.first) {
            case Parameters::ValueType::BOOLEAN:
                args.set(index, value.second.valueBool);
                break;
            case Parameters::ValueType::NUMBER:
                args.set(index, value.second.valueNumber);
                break;
            case Parameters::ValueType::STRING:
                args.set(index, value.second.valueString);
                break;
            }
        }
        mFunctionMap[ID].call<val>("apply", val::undefined(), args);
    }
}
