#include "../catch.hpp"
#include "../functions/function8.cpp"

TEST_CASE( "Testing function8 1", "[function8]" ) {
    REQUIRE(function8(3,5,"The answer is ",{1,2,3}) == std::make_pair("The answer is 15", std::vector<int>{4,5,6}));
}

TEST_CASE( "Testing function8 2", "[function8]" ) {
    REQUIRE(function8(2,6,"The answer is ",{4,5,6}) == std::make_pair("The answer is 12", std::vector<int>{6,7,8}));
}