#include "catch.hpp"
#include "../functions/function4.cpp"

TEST_CASE("Test function4 number 1", "[function4]") {
    REQUIRE(function4(6, "Hello", {2, 5, 8}) == 54.0);
}

TEST_CASE("Test function4 number 2", "[function4]") {
    REQUIRE(function4(9, "World", {1, 3, 4}) == 66.0);
}