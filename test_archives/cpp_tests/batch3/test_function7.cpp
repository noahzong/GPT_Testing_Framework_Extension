#include "../catch.hpp"
#include "../functions/function7.cpp"

TEST_CASE( "Test function7_1", "[function7_1]" ) {
    REQUIRE( function7("Hello", 2, {3, 4, 5}) == 22 );
}

TEST_CASE( "Test function7_2", "[function7_2]" ) {
    REQUIRE( function7("World", 3, {1,2,3,4,5}) == 30.0 );
}