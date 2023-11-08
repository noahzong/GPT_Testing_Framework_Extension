#include "../catch.hpp"
#include "../functions/function8.cpp"

TEST_CASE("Test 1 function8", "[function8]") {
    REQUIRE(function8(1, "abcd", true, 3) == 4); 
}

TEST_CASE("Test 2 function8", "[function8]") {
    REQUIRE(function8(2, "efgh", false, 0) == 4); 
}