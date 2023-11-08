#include "../catch.hpp"
#include "../functions/function1.cpp"

TEST_CASE("test_function1_1") {
    REQUIRE(function1("abc", 3, 1.5, {2, 4, 6}) == "abcabcabc27.0");
}

TEST_CASE("test_function1_2") {
    REQUIRE(function1("xyz", 4, 2.5, {3, 6, 9}) == "xyzxyzxyzxyz112.5");
}