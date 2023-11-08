#include "../catch.hpp"
#include "../functions/function5.cpp"

TEST_CASE("Function5 tests")
{
    SECTION("Test 1")
    {
        REQUIRE(function5(4, 5.2, "hello", {"a", "b", "c"}) == std::make_pair(9.2, {"helloa", "hellob", "helloc"}));
    }
    
    SECTION("Test 2")
    {
        REQUIRE(function5(2, 3.3, "world", {"d", "e"}) == std::make_pair(5.3, {"worldd", "worlde"}));
    }
}