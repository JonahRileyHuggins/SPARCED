#include "amici/sundials_matrix_wrapper.h"
#include "sundials/sundials_types.h"

#include <array>
#include <algorithm>

namespace amici {
namespace model_Basic_model {

static constexpr std::array<sunindextype, 3> dxdotdw_colptrs_Basic_model_ = {
    0, 3, 6
};

void dxdotdw_colptrs_Basic_model(SUNMatrixWrapper &dxdotdw){
    dxdotdw.set_indexptrs(gsl::make_span(dxdotdw_colptrs_Basic_model_));
}
} // namespace amici
} // namespace model_Basic_model