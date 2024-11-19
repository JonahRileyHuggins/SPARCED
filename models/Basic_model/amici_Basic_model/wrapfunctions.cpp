#include "amici/model.h"
#include "wrapfunctions.h"
#include "Basic_model.h"

namespace amici {
namespace generic_model {

std::unique_ptr<amici::Model> getModel() {
    return std::unique_ptr<amici::Model>(
        new amici::model_Basic_model::Model_Basic_model());
}


} // namespace generic_model

} // namespace amici
