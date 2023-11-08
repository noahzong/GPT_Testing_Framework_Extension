#include "../catch.hpp"
#include "../functions/function9.cpp"

TEST_CASE( "Testing the process_data() function", "[process_data]" ) {
    SECTION("Testing process_data() with different inputs") {
        REQUIRE(function9("Test", 1, {1, 2, 3}).process_data() == 0);
        REQUIRE(function9("Test2", 2, {3, 4, 5}).process_data() == 0);
    }
}