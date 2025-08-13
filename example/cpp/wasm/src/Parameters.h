#pragma once

#include <string>
#include <utility>
#include <vector>

class Parameters {
public:
    // data type notified parameters
    enum class ValueType : int {
        BOOLEAN,
        NUMBER,
        STRING,
    };

private:
    // parameter information
    class Parameter {
    public:
        bool valueBool;
        int valueNumber;
        std::string valueString;

    public:
        Parameter()
        : valueBool(false)
        , valueNumber(0)
        , valueString("") {
        }

        virtual ~Parameter() {
        }
    };

private:
    // notified parameters
    std::vector<std::pair<ValueType, Parameter>> mParameterList;

public:
    // constructor
    Parameters();

    // destructor
    virtual ~Parameters();

    // add boolean parameter
    void addBool(bool value);

    // add number parameter
    void addNumber(int value);

    // add string paramter
    void addString(const std::string& value);

    // get all paramters
    const std::vector<std::pair<ValueType, Parameter>>& getParameterList() const;
};