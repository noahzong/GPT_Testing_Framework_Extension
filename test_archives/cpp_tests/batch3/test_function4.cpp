#include "../catch.hpp"
#include "../functions/function4.cpp"

TEST_CASE("Test function4_1") {
    REQUIRE(function4(1, 2, 3.0, 4.0, "hi", "there", true, true) == "14hitherTrue");
}

TEST_CASE("Test function4_2") {
    REQUIRE(function4(3, 4, 2.0, 4.1, "hello", "world", false, true) == "7hello worldFalse");
}