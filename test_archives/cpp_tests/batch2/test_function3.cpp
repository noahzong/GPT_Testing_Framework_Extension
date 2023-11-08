#include "../catch.hpp"
#include "../functions/function3.cpp"

TEST_CASE("Test function3 1", "[function3]") {
    REQUIRE(function3("yes", 2, 3.5) == 17.0);
}

TEST_CASE("Test function3 2", "[function3]") {
    REQUIRE(function3("no", 4, 6.2) == 19.8);
}