#include "../catch.hpp"
#include "../functions/function3.cpp"

TEST_CASE( "Test function3 1", "[function3]" ) {
    REQUIRE( function3(1, 2, "name") == 21.5 );
}

TEST_CASE( "Test function3 2", "[function3]" ) {
    REQUIRE( function3(2, 4, "age") == 34.75 );
}