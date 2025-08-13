#include "Parameters.h"

using namespace std;

Parameters::Parameters() {
}

Parameters::~Parameters() {
}

void Parameters::addBool(bool value) {
    mParameterList.push_back({ValueType::BOOLEAN, Parameter()});
    mParameterList[mParameterList.size() - 1].second.valueBool = value;
}

void Parameters::addNumber(int value) {
    mParameterList.push_back({ValueType::NUMBER, Parameter()});
    mParameterList[mParameterList.size() - 1].second.valueNumber = value;
}

void Parameters::addString(const string& value) {
    mParameterList.push_back({ValueType::STRING, Parameter()});
    mParameterList[mParameterList.size() - 1].second.valueString = value;
}

const vector<pair<Parameters::ValueType, Parameters::Parameter>>&
Parameters::getParameterList() const {
    return mParameterList;
}