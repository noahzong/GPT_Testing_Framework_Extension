#include "../catch.hpp"
#include "../functions/function2.cpp"

TEST_CASE("function2 should return the correct value", "[function2]") {
    REQUIRE(function2("hello", 1, std::vector<int>{2,3}) == 11);
    REQUIRE(function2("world", 3, std::vector<int>{4,5,6}) == 23);
}