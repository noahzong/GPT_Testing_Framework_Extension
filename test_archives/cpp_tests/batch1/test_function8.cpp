#include "../catch.hpp"
#include "../functions/function8.cpp"

TEST_CASE( "Testing function8 with the first test case" ) {
    REQUIRE( function8("Hello ", 10, {1, 2}, true) == "Hello 1210" );
}

TEST_CASE( "Testing function8 with the second test case" ) {
    REQUIRE( function8("Hi ", 15, {4, 5}, false) == "4515" );
}