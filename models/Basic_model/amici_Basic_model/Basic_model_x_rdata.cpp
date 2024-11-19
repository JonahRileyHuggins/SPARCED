#include "amici/symbolic_functions.h"
#include "amici/defines.h"
#include "sundials/sundials_types.h"

#include <array>

#include "tcl.h"
#include "x.h"

namespace amici {
namespace model_Basic_model {

void x_rdata_Basic_model(realtype *x_rdata, const realtype *x, const realtype *tcl){
    x_rdata[0] = L;
    x_rdata[1] = R;
    x_rdata[2] = LR;
}

} // namespace amici
} // namespace model_Basic_model