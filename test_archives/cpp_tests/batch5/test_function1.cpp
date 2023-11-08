#include "../catch.hpp"
#include "../functions/function1.cpp"

TEST_CASE( "Tests for function1 class", "[function1]" ) {
    SECTION("Test for compute()") {
        function1 object("hello", 3, 4.5, true, {2, 4, 6});
        REQUIRE(object.compute() == "hello34.5True[2, 4, 6]");
    }
}