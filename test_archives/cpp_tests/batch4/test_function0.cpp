#include "../catch.hpp"
#include "../functions/function0.cpp"

TEST_CASE( "Test function0_1", "[function0]" ) {
    REQUIRE( function0('A', 'B', 5, 10.5, true) == "AB510.5" );
}

TEST_CASE( "Test function0_2", "[function0]" ) {
    REQUIRE( function0('C', 'D', 3, 7.2, false) == "CD37.2" );
}