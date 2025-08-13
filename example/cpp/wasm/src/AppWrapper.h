#pragma once

#include <memory>
#include <string>
#include <emscripten/bind.h>

class AppWrapper {
private:
    static AppWrapper* mInstance;
    bool mOnOff;
    float mValue;
    std::string mTime;

public:
    static AppWrapper& getInstance();

    static void releaseInstance();

    bool addCallback(uint16_t id, emscripten::val func);

    bool removeCallback(uint16_t id);
	
	void update(int cycle);
	
	int setParameters(bool onoff, float value, std::string time);

private:
    AppWrapper();

    virtual ~AppWrapper();
};