#include "../catch.hpp"
#include "../functions/function0.cpp"

TEST_CASE( "function0 multiply_result", "[multiply_result]" ) {
    SECTION("Correct results") {
        REQUIRE(function0(1, 2.5, 'test', {2, 3}).multiply_result() == 15);
        REQUIRE(function0(2, 3.5, 'test', {1, 2}).multiply_result() == 14);
        REQUIRE(function0(3, 4.5, 'test', {3, 4}).multiply_result() == 162);
    }
}