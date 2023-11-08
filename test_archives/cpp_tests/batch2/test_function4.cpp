#include "../catch.hpp"
#include "../functions/function4.cpp"

TEST_CASE("Test function4", "[function4]") {
  SECTION("Correct tests") {
    REQUIRE(function4(1, 2, 3, "abc", {1, 2, 3}) == 15);
    REQUIRE(function4(2, 4, 6, "def", {4, 5, 6}) == 30);
  }
}