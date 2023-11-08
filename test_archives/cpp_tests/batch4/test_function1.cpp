#include "../catch.hpp"
#include "../functions/function1.cpp"

TEST_CASE( "Test function1 1", "[function1]" ) {
    REQUIRE( function1("foo", 1, true) == 12 );
}

TEST_CASE( "Test function1 2", "[function1]" ) {
    REQUIRE( function1("bar", 2, false) == 3 );
}