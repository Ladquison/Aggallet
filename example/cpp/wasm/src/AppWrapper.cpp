#include "AppWrapper.h"
#include "CallbackUtility.h"
#include "WasmCallbackId.h"

using namespace std;
using namespace emscripten;

AppWrapper* AppWrapper::mInstance = nullptr;

AppWrapper::AppWrapper()
    : mOnOff(false)
    , mValue(0.0f)
    , mTime("") {
}

AppWrapper::~AppWrapper() {
}

AppWrapper& AppWrapper::getInstance() {
    if (mInstance == nullptr) {
        mInstance = new AppWrapper();
    }
    return *mInstance;
}

void AppWrapper::releaseInstance() {
    if (mInstance != nullptr) {
        delete mInstance;
        mInstance = nullptr;
    }
}

bool AppWrapper::addCallback(uint16_t id, emscripten::val func) {
    return CallbackUtility::addFunction(static_cast<FUNCTION_ID>(id), func);
}

bool AppWrapper::removeCallback(uint16_t id) {
	return CallbackUtility::removeFunction(static_cast<FUNCTION_ID>(id));
}

void AppWrapper::update(int cycle) {
    static int count = 0;
    count += cycle;
    if (1000 <= count) {
        count -= 1000;
        Parameters params;
        params.addBool(mOnOff);
        params.addNumber(static_cast<int>(mValue * 10));
        params.addString(mTime + "_" + mTime);
        CallbackUtility::call(FUNCTION_ID::RESPOND_PARAMETERS, params);
    }
}

int AppWrapper::setParameters(bool onoff, float value, std::string time) {
    static int count = 0;
    mOnOff = onoff;
    mValue = value;
    mTime = time;
	return ++count;
}
