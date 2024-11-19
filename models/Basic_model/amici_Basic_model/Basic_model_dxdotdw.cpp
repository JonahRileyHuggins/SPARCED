#include "amici/symbolic_functions.h"
#include "amici/defines.h"
#include "sundials/sundials_types.h"

#include <array>

#include "p.h"
#include "k.h"
#include "w.h"
#include "h.h"
#include "x.h"
#include "dxdotdw.h"

namespace amici {
namespace model_Basic_model {

void dxdotdw_Basic_model(realtype *dxdotdw, const realtype t, const realtype *x, const realtype *p, const realtype *k, const realtype *h, const realtype *w){
    dxdot0_dflux_r0 = -1.0;  // dxdotdw[0]
    dxdot1_dflux_r0 = -1.0;  // dxdotdw[1]
    dxdot2_dflux_r0 = 1.0;  // dxdotdw[2]
    dxdot0_dflux_r1 = 1.0;  // dxdotdw[3]
    dxdot1_dflux_r1 = 1.0;  // dxdotdw[4]
    dxdot2_dflux_r1 = -1.0;  // dxdotdw[5]
}

} // namespace amici
} // namespace model_Basic_model