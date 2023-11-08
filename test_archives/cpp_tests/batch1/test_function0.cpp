#include "../catch.hpp"
#include "../functions/function0.cpp"

TEST_CASE("Test function0_1", "[function0]") {
	REQUIRE(function0(1, 2.3, "hello", true) == 3.3);
}

TEST_CASE("Test function0_2", "[function0]") {
	REQUIRE(function0(2, 4.6, "world", false) == 0);
}

TEST_CASE("Test function0_3", "[function0]") {
	REQUIRE(function0(3, 6.9, "hello", false) == 6.9);
}

TEST_CASE("Test function0_4", "[function0]") {
	REQUIRE(function0(4, 9.2, "world", true) == 4);
}