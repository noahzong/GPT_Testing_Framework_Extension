#include "../catch.hpp"
#include "../functions/function6.cpp"

TEST_CASE("Test function6_1", "[function6]") {
    REQUIRE(function6("John", 20, true, true) == "John is 20 years old. They like pizza. They are an active member.");
}

TEST_CASE("Test function6_2", "[function6]") {
    REQUIRE(function6("Mary", 18, false, false) == "Mary is 18 years old. They don't like pizza. They are not an active member.");
}