#include "../catch.hpp"
#include "../functions/function6.cpp"

TEST_CASE( "Test function 6", "[function6]" ) {
	REQUIRE( function6("John", 20, true, 3) == 28.35 );
	REQUIRE( function6("Jane", 25, false, 4) == 42.0 );
}