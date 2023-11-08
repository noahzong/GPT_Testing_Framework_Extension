#include "../catch.hpp"
#include "../functions/function7.cpp"

TEST_CASE( "Test function7_1", "[function7_1]" ) {
    REQUIRE(function7(1, 2.0, true, "test", {1, 2, 3}, {{"a", 1}, {"b", 2}}) == 13);
}

TEST_CASE( "Test function7_2", "[function7_2]" ) {
    REQUIRE(function7(2, 3.3, false, "", {}, {}) == 5.3);
}