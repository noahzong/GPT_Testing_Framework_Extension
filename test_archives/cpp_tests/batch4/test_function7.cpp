#include "../catch.hpp"
#include "../functions/function7.cpp"

TEST_CASE( "Testing function7", "[function7]" ) {

    SECTION( "Test function7_1" ) {
        REQUIRE( function7(1, "abc", 2.5, {"a", "b"}) == 4.5 );
    }

    SECTION( "Test function7_2" ) {
        REQUIRE( function7(3, "xyz", 3.5, {"x", "y"}) == 12.5 );
    }

}