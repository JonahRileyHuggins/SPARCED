#include "amici/symbolic_functions.h"
#include "amici/defines.h"
#include "sundials/sundials_types.h"

#include <array>

#include "p.h"
#include "k.h"
#include "w.h"
#include "h.h"
#include "x.h"

namespace amici {
namespace model_Basic_model {

void y_Basic_model(realtype *y, const realtype t, const realtype *x, const realtype *p, const realtype *k, const realtype *h, const realtype *w){
    y[0] = L;
    y[1] = R;
    y[2] = LR;
    y[3] = 1.0;
}

} // namespace amici
} // namespace model_Basic_model