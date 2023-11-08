#include "../catch.hpp"
#include "../functions/function1.cpp"

TEST_CASE( "Testing function1_1", "[function1]" ) {
    REQUIRE( function1("string", 2, true) == "string2" );
}

TEST_CASE( "Testing function1_2", "[function1]" ) {
    REQUIRE( function1("string", 2, false) == "string4" );
}