#include "amici/symbolic_functions.h"
#include "amici/defines.h"
#include "sundials/sundials_types.h"

#include <array>

#include "p.h"
#include "k.h"

namespace amici {
namespace model_Basic_model {

void x0_Basic_model(realtype *x0, const realtype t, const realtype *p, const realtype *k){
    x0[1] = 100.0;
}

} // namespace amici
} // namespace model_Basic_model