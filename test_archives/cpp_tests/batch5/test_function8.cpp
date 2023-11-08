#include "../catch.hpp"
#include "../functions/function8.cpp"

TEST_CASE("combine_vars() function works properly", "[function8]") {
    function8 function8_test(1, 2, 3);
    REQUIRE(function8_test.combine_vars() == "variable00.0False[](){}123");
}