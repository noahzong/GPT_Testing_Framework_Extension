#include "../catch.hpp"
#include "../functions/function1.cpp"

TEST_CASE("function1 - test 1", "[function1]") {
    REQUIRE(function1("abc", {1, 2, 3}) == 90);
}

TEST_CASE("function1 - test 2", "[function1]") {
    REQUIRE(function1("xyz", {4, 5, 6}, 5) == 45);
}