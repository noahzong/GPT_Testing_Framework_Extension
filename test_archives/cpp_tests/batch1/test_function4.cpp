#include "../catch.hpp"
#include "../functions/function4.cpp"

TEST_CASE( "Testing function4", "[function4]" ) {
    REQUIRE( function4(1, 2, 3) == 'b' );
    REQUIRE( function4(2, 4, 6) == 'b' );
}