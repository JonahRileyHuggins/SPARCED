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

void Jy_Basic_model(realtype *Jy, const int iy, const realtype *p, const realtype *k, const realtype *y, const realtype *sigmay, const realtype *my){
    switch(iy) {
        case 0:
            Jy[0] = 0.5*std::log(2*amici::pi*std::pow(sigma_yL, 2)) + 0.5*std::pow(-myL + yL, 2)/std::pow(sigma_yL, 2);
            break;
        case 1:
            Jy[0] = 0.5*std::log(2*amici::pi*std::pow(sigma_yR, 2)) + 0.5*std::pow(-myR + yR, 2)/std::pow(sigma_yR, 2);
            break;
        case 2:
            Jy[0] = 0.5*std::log(2*amici::pi*std::pow(sigma_yLR, 2)) + 0.5*std::pow(-myLR + yLR, 2)/std::pow(sigma_yLR, 2);
            break;
        case 3:
            Jy[0] = 0.5*std::log(2*amici::pi*std::pow(sigma_yCytoplasm, 2)) + 0.5*std::pow(-myCytoplasm + yCytoplasm, 2)/std::pow(sigma_yCytoplasm, 2);
            break;
    }
}

} // namespace amici
} // namespace model_Basic_model