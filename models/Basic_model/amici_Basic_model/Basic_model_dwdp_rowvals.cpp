#include "amici/sundials_matrix_wrapper.h"
#include "sundials/sundials_types.h"

#include <array>
#include <algorithm>

namespace amici {
namespace model_Basic_model {

static constexpr std::array<sunindextype, 2> dwdp_rowvals_Basic_model_ = {
    0, 1
};

void dwdp_rowvals_Basic_model(SUNMatrixWrapper &dwdp){
    dwdp.set_indexvals(gsl::make_span(dwdp_rowvals_Basic_model_));
}
} // namespace amici
} // namespace model_Basic_model