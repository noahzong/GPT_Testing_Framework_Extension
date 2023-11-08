#include "../catch.hpp"
#include "../functions/function7.cpp"

TEST_CASE( "Testing function7 with test_function7_1" ) {
    REQUIRE( function7("Hello", 1, 2, true) == "Hello 3" );
}

TEST_CASE( "Testing function7 with test_function7_2" ) {
    REQUIRE( function7("World", 3, 4, false) == "World 12" );
}