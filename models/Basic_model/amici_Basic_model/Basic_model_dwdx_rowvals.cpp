#include "amici/sundials_matrix_wrapper.h"
#include "sundials/sundials_types.h"

#include <array>
#include <algorithm>

namespace amici {
namespace model_Basic_model {

static constexpr std::array<sunindextype, 3> dwdx_rowvals_Basic_model_ = {
    0, 0, 1
};

void dwdx_rowvals_Basic_model(SUNMatrixWrapper &dwdx){
    dwdx.set_indexvals(gsl::make_span(dwdx_rowvals_Basic_model_));
}
} // namespace amici
} // namespace model_Basic_model