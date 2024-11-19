#include "amici/symbolic_functions.h"
#include "amici/defines.h"
#include "sundials/sundials_types.h"

#include <array>

#include "p.h"
#include "k.h"
#include "sigmay.h"

namespace amici {
namespace model_Basic_model {

void sigmay_Basic_model(realtype *sigmay, const realtype t, const realtype *p, const realtype *k){
    sigma_yL = 1.0;  // sigmay[0]
    sigma_yR = 1.0;  // sigmay[1]
    sigma_yLR = 1.0;  // sigmay[2]
    sigma_yCytoplasm = 1.0;  // sigmay[3]
}

} // namespace amici
} // namespace model_Basic_model