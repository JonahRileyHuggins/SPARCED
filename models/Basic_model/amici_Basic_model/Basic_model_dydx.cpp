#include "amici/symbolic_functions.h"
#include "amici/defines.h"
#include "sundials/sundials_types.h"

#include <array>

#include "p.h"
#include "k.h"
#include "w.h"
#include "h.h"
#include "x.h"
#include "dwdx.h"

namespace amici {
namespace model_Basic_model {

void dydx_Basic_model(realtype *dydx, const realtype t, const realtype *x, const realtype *p, const realtype *k, const realtype *h, const realtype *w, const realtype *dwdx){
    dydx[0] = 1;
    dydx[5] = 1;
    dydx[10] = 1;
}

} // namespace amici
} // namespace model_Basic_model