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

namespace amici {
namespace model_Basic_model {

void w_Basic_model(realtype *w, const realtype t, const realtype *x, const realtype *p, const realtype *k, const realtype *h, const realtype *tcl){
    flux_r0 = L*R*k1;  // w[0]
    flux_r1 = LR*k2;  // w[1]
}

} // namespace amici
} // namespace model_Basic_model