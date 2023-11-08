#include "../catch.hpp"
#include "../functions/function9.cpp"

TEST_CASE( "Testing function9 for two cases", "[function9]" ) {
    REQUIRE( function9(1, 2.5, "foo", {1,2,3}) == 12.5 );
    REQUIRE( function9(4, 7.2, "bar", {3,4,5}) == 26.2 );
}