#include "amici/sundials_matrix_wrapper.h"
#include "sundials/sundials_types.h"

#include <array>
#include <algorithm>

namespace amici {
namespace model_Basic_model {

static constexpr std::array<sunindextype, 4> dwdx_colptrs_Basic_model_ = {
    0, 1, 2, 3
};

void dwdx_colptrs_Basic_model(SUNMatrixWrapper &dwdx){
    dwdx.set_indexptrs(gsl::make_span(dwdx_colptrs_Basic_model_));
}
} // namespace amici
} // namespace model_Basic_model