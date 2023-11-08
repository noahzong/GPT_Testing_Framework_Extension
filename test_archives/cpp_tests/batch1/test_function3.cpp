#include "../catch.hpp"
#include "../functions/function3.cpp"

TEST_CASE( "function3_1 tests", "[function3]" ) {
    REQUIRE( function3('a', 1, {'x': 2, 'y': 3}, True) == "a15True" );
}

TEST_CASE( "function3_2 tests", "[function3]" ) {
    REQUIRE( function3('b', 2, {'x': 4, 'y': 5}, False) == "b29False" );
}