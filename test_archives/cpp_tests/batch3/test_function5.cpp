#include "../catch.hpp"
#include "../functions/function5.cpp"
 
TEST_CASE( "Function5 tests", "[function5]" ) {
    REQUIRE( function5(1, 2, 3) == 6 );
    REQUIRE( function5(2, 4, 6) == 12 );
}