#include "../catch.hpp"
#include "../functions/function9.cpp"

TEST_CASE( "Tests for function9", "[function9]" ) {
    REQUIRE( function9("abc", "def", 1, 2.3) == 9.3 );
    REQUIRE( function9("xyz", "uvw", 5, 7.8) == 18.8 );
}