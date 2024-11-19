#include "amici/symbolic_functions.h"
#include "amici/defines.h"
#include "sundials/sundials_types.h"

#include <array>

#include "x_rdata.h"

namespace amici {
namespace model_Basic_model {

void x_solver_Basic_model(realtype *x_solver, const realtype *x_rdata){
    x_solver[0] = L;
    x_solver[1] = R;
    x_solver[2] = LR;
}

} // namespace amici
} // namespace model_Basic_model