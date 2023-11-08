#include "../catch.hpp"
#include "../functions/function6.cpp"

TEST_CASE("function6", "[function6]") {
    SECTION("sum, concat and list average") {
        REQUIRE(function6(1, 2, "a", "b",  {1, 2},  {3, 4}).get_sum() == 3);
        REQUIRE(function6(1, 2, "a", "b",  {1, 2},  {3, 4}).get_concat() == "ab");
        REQUIRE(function6(1, 2, "a", "b",  {1, 2},  {3, 4}).get_lst_avg() == 2.5);
        REQUIRE(function6(2, 3, "c", "d",  {4, 5},  {6, 7}).get_sum() == 5);
        REQUIRE(function6(2, 3, "c", "d",  {4, 5},  {6, 7}).get_concat() == "cd");