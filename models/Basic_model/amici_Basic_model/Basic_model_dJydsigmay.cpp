#include "amici/symbolic_functions.h"
#include "amici/defines.h"
#include "sundials/sundials_types.h"

#include <array>

#include "y.h"
#include "my.h"
#include "p.h"
#include "k.h"
#include "sigmay.h"

namespace amici {
namespace model_Basic_model {

void dJydsigmay_Basic_model(realtype *dJydsigmay, const int iy, const realtype *p, const realtype *k, const realtype *y, const realtype *sigmay, const realtype *my){
    switch(iy) {
        case 0:
            dJydsigmay[0] = 1.0/sigma_yL - 1.0*std::pow(-myL + yL, 2)/std::pow(sigma_yL, 3);
            break;
        case 1:
            dJydsigmay[1] = 1.0/sigma_yR - 1.0*std::pow(-myR + yR, 2)/std::pow(sigma_yR, 3);
            break;
        case 2:
            dJydsigmay[2] = 1.0/sigma_yLR - 1.0*std::pow(-myLR + yLR, 2)/std::pow(sigma_yLR, 3);
            break;
        case 3:
            dJydsigmay[3] = 1.0/sigma_yCytoplasm - 1.0*std::pow(-myCytoplasm + yCytoplasm, 2)/std::pow(sigma_yCytoplasm, 3);
            break;
    }
}

} // namespace amici
} // namespace model_Basic_model