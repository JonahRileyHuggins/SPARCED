#include "amici/sundials_matrix_wrapper.h"
#include "sundials/sundials_types.h"

#include <array>
#include <algorithm>

namespace amici {
namespace model_Basic_model {

static constexpr std::array<sunindextype, 3> dwdp_colptrs_Basic_model_ = {
    0, 1, 2
};

void dwdp_colptrs_Basic_model(SUNMatrixWrapper &dwdp){
    dwdp.set_indexptrs(gsl::make_span(dwdp_colptrs_Basic_model_));
}
} // namespace amici
} // namespace model_Basic_model