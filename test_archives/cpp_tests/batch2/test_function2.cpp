#include "catch.hpp"
#include "../functions/function2.cpp"

TEST_CASE("Test function2", "[function2]")
{
    REQUIRE(function2(1, 2, "abc", {1, 2, 3}, true) == 12);
    REQUIRE(function2(2, 4, "def", {4, 5, 6}, false) == 7);
    REQUIRE(function2(3, 6, "ghi", {7, 8, 9}, true) == 18);
    REQUIRE(function2(4, 8, "jkl", {10, 11, 12}, false) == 5);
}