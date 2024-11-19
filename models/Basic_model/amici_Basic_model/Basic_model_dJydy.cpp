#include "amici/symbolic_functions.h"
#include "amici/defines.h"
#include "sundials/sundials_types.h"

#include <array>

#include "y.h"
#include "my.h"
#include "p.h"
#include "k.h"
#include "sigmay.h"
#include "dJydy.h"

namespace amici {
namespace model_Basic_model {

void dJydy_Basic_model(realtype *dJydy, const int iy, const realtype *p, const realtype *k, const realtype *y, const realtype *sigmay, const realtype *my){
    switch(iy) {
        case 0:
            dJydy[0] = (-1.0*myL + 1.0*yL)/std::pow(sigma_yL, 2);
            break;
        case 1:
            dJydy[0] = (-1.0*myR + 1.0*yR)/std::pow(sigma_yR, 2);
            break;
        case 2:
            dJydy[0] = (-1.0*myLR + 1.0*yLR)/std::pow(sigma_yLR, 2);
            break;
        case 3:
            dJydy[0] = (-1.0*myCytoplasm + 1.0*yCytoplasm)/std::pow(sigma_yCytoplasm, 2);
            break;
    }
}

} // namespace amici
} // namespace model_Basic_model