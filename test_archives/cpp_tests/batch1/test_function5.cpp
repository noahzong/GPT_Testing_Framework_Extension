#include "../catch.hpp"
#include "../functions/function5.cpp"

TEST_CASE("Testing function5 with 1, 'abc', 2.5, [1,2,3]") {
    REQUIRE(function5(1, 'abc', 2.5, std::vector<int>{1,2,3}) == 9.5);
}

TEST_CASE("Testing function5 with 3, 'xy', 4.8, [4,5,6,7]") {
    REQUIRE(function5(3, 'xy', 4.8, std::vector<int>{4,5,6,7}) == 13.8);
}