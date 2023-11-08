#include "../catch.hpp"
#include "../functions/function9.cpp"

TEST_CASE( "Testing function9_1", "[function9]" ) {
    REQUIRE( function9("abc", 3, true) == "abc3" );
}

TEST_CASE( "Testing function9_2", "[function9]" ) {
    REQUIRE( function9("def", 5, false) == "" );
}