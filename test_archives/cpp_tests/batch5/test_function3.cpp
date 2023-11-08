#include "../catch.hpp"
#include "../functions/function3.cpp"

TEST_CASE("Function3 initialization", "[function3]") {
    Function3 function3("John", 25, "Male", "123 Main Street", "555-555-5555");

    REQUIRE(function3.name == "John");
    REQUIRE(function3.age == 25);
    REQUIRE(function3.gender == "Male");
    REQUIRE(function3.address == "123 Main Street");
    REQUIRE(function3.phone_number == "555-555-5555");
}

TEST_CASE("Function3 calculate value", "[function3]") {
    Function3 function3("John", 25, "Male", "123 Main Street", "555-555-5555");

    REQUIRE(function3.calculate_value() == 25 + 555555555);
}