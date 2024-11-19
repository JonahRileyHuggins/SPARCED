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
#include "dwdp.h"

namespace amici {
namespace model_Basic_model {

void dwdp_Basic_model(realtype *dwdp, const realtype t, const realtype *x, const realtype *p, const realtype *k, const realtype *h, const realtype *w, const realtype *tcl, const realtype *dtcldp){
    dflux_r0_dk1 = L*R;  // dwdp[0]
    dflux_r1_dk2 = LR;  // dwdp[1]
}

} // namespace amici
} // namespace model_Basic_model