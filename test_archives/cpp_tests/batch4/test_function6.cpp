#include "../catch.hpp"
#include "../functions/function6.cpp"

TEST_CASE("Test function6_1", "[function6]") {
    REQUIRE(function6("a", 2, {1,2,3}, 4.2, true) == 424.0);
}

TEST_CASE("Test function6_2", "[function6]") {
    REQUIRE(function6("b", 3, {4,5}, 10.2, false) == 3060.0);
}