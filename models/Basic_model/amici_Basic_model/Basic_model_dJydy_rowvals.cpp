#include "amici/sundials_matrix_wrapper.h"
#include "sundials/sundials_types.h"

#include <array>
#include <algorithm>

namespace amici {
namespace model_Basic_model {

static constexpr std::array<std::array<sunindextype, 1>, 4> dJydy_rowvals_Basic_model_ = {{
    {0}, 
    {0}, 
    {0}, 
    {0}, 
}};

void dJydy_rowvals_Basic_model(SUNMatrixWrapper &dJydy, int index){
    dJydy.set_indexvals(gsl::make_span(dJydy_rowvals_Basic_model_[index]));
}
} // namespace amici
} // namespace model_Basic_model