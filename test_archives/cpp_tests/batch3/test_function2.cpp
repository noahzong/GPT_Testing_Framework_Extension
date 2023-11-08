#include "../catch.hpp"
#include "../functions/function2.cpp"
 
TEST_CASE( "Tests for function2", "[function2]" ) {
    REQUIRE( function2("ABC", 1, 2.3) == 6 );
    REQUIRE( function2("ABCD", 2, 3.5) == 28 );
}