#include "amici/symbolic_functions.h"
#include "amici/defines.h"
#include "sundials/sundials_types.h"

#include <array>

#include "tcl.h"
#include "p.h"
#include "k.h"
#include "w.h"
#include "h.h"
#include "x.h"
#include "dwdx.h"

namespace amici {
namespace model_Basic_model {

void dwdx_Basic_model(realtype *dwdx, const realtype t, const realtype *x, const realtype *p, const realtype *k, const realtype *h, const realtype *w, const realtype *tcl){
    dflux_r0_dL = R*k1;  // dwdx[0]
    dflux_r0_dR = L*k1;  // dwdx[1]
    dflux_r1_dLR = k2;  // dwdx[2]
}

} // namespace amici
} // namespace model_Basic_model