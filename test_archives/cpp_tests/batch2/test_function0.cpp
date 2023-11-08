#include "../catch.hpp"
#include "../functions/function0.cpp"

TEST_CASE("Test function0_1", "[function0]") {
    REQUIRE(function0(1, 2.3, "four", {5, 6}) == 9.3);
}

TEST_CASE("Test function0_2", "[function0]") {
    REQUIRE(function0(2, 4.6, "eight", {10, 12}) == 13.6);
}