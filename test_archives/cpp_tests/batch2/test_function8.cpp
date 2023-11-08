#include "../catch.hpp"
#include "../functions/function8.cpp"

TEST_CASE( "Test function8_1", "[function8]" ) {
    REQUIRE( function8("hello", {1, 2, 3}, true, 4, 5.2) == "hello4" );
}

TEST_CASE( "Test function8_2", "[function8]" ) {
    REQUIRE( function8("world", {4, 5, 6}, false, 7, 8.3) == "[4, 5, 6]8.3" );
}