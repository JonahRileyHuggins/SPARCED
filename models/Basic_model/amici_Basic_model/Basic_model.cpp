#include "Basic_model.h"
#include <array>

namespace amici {

namespace model_Basic_model {

std::array<const char*, 2> parameterNames = {
    "k1",
"k2",
};

std::array<const char*, 0> fixedParameterNames = {
    
};

std::array<const char*, 3> stateNames = {
    "L",
"R",
"LR",
};

std::array<const char*, 4> observableNames = {
    "L",
"R",
"LR",
"Cytoplasm",
};

std::array<const char*, 2> expressionNames = {
    "flux_r0",
"flux_r1",
};

std::array<const char*, 2> parameterIds = {
    "k1",
"k2",
};

std::array<const char*, 0> fixedParameterIds = {
    
};

std::array<const char*, 3> stateIds = {
    "L",
"R",
"LR",
};

std::array<const char*, 4> observableIds = {
    "yL",
"yR",
"yLR",
"yCytoplasm",
};

std::array<const char*, 2> expressionIds = {
    "flux_r0",
"flux_r1",
};

} // namespace model_Basic_model

} // namespace amici
