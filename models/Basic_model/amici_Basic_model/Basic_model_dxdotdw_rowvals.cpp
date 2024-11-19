#include "amici/sundials_matrix_wrapper.h"
#include "sundials/sundials_types.h"

#include <array>
#include <algorithm>

namespace amici {
namespace model_Basic_model {

static constexpr std::array<sunindextype, 6> dxdotdw_rowvals_Basic_model_ = {
    0, 1, 2, 0, 1, 2
};

void dxdotdw_rowvals_Basic_model(SUNMatrixWrapper &dxdotdw){
    dxdotdw.set_indexvals(gsl::make_span(dxdotdw_rowvals_Basic_model_));
}
} // namespace amici
} // namespace model_Basic_model