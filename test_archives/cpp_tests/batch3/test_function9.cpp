#include "../catch.hpp"
#include "../functions/function9.cpp"

TEST_CASE("Test function9 1", "[function9]") {
  REQUIRE(function9("total = ", 1, 2, 3, std::vector<int>{1,2,3}) == "total = 24");
}

TEST_CASE("Test function9 2", "[function9]") {
  REQUIRE(function9("sum = ", 2, 4, 6, std::vector<int>{3,5,7}) == "sum = 51");
}