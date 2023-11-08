#include "../catch.hpp"
#include "../functions/function3.cpp"

TEST_CASE("Test function3_1", "[function3]") 
{
    REQUIRE(function3("2", "3", 4.5, 3) == 5.0);
}

TEST_CASE("Test function3_2", "[function3]") 
{
    REQUIRE(function3("4", "6", 2.2, 8) == 6.8);
}