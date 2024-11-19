#include "amici/symbolic_functions.h"
#include "amici/defines.h"
#include "sundials/sundials_types.h"

#include <array>

#include "p.h"
#include "k.h"
#include "w.h"
#include "h.h"
#include "x.h"
#include "xdot.h"

namespace amici {
namespace model_Basic_model {

void xdot_Basic_model(realtype *xdot, const realtype t, const realtype *x, const realtype *p, const realtype *k, const realtype *h, const realtype *w){
    xdot0 = -1.0*flux_r0 + 1.0*flux_r1;  // xdot[0]
    xdot1 = -1.0*flux_r0 + 1.0*flux_r1;  // xdot[1]
    xdot2 = 1.0*flux_r0 - 1.0*flux_r1;  // xdot[2]
}

} // namespace amici
} // namespace model_Basic_model