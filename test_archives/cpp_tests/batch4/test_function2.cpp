#include "../catch.hpp"
#include "../functions/function2.cpp"

TEST_CASE( "Test function2 with inputs test, 1, 2, [1, 2, 3]", "[function2]" ) {
    REQUIRE( function2("test", 1, 2, {1, 2, 3}) == Approx(4.0) );
}

TEST_CASE( "Test function2 with inputs test, 2, 4, [1, 2, 3, 4, 5]", "[function2]" ) {
    REQUIRE( function2("test", 2, 4, {1, 2, 3, 4, 5}) == Approx(4.8) );
}