#include "../catch.hpp"
#include "../functions/function0.cpp"

TEST_CASE("Test function0_1", "[function0]") {
    REQUIRE(function0(1, 2, 'a', 'b', 3) == 9);
}

TEST_CASE("Test function0_2", "[function0]") {
    REQUIRE(function0(2, 4, 'c', 'd', 5) == 30);
}