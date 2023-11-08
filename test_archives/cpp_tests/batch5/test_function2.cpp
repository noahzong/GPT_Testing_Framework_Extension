#include "../catch.hpp"
#include "../functions/function2.cpp"

TEST_CASE("test function2 name", "[function2]") {
    function2 function2_obj ("John", 12, 4, "English");
    REQUIRE(function2_obj.name == "John");
}

TEST_CASE("test function2 age", "[function2]") {
    function2 function2_obj ("John", 12, 4, "English");
    REQUIRE(function2_obj.age == 12);
}

TEST_CASE("test function2 grade", "[function2]") {
    function2 function2_obj ("John", 12, 4, "English");
    REQUIRE(function2_obj.grade == 4);
}

TEST_CASE("test function2 language", "[function2]") {
    function2 function2_obj ("John", 12, 4, "English");
    REQUIRE(function2_obj.language == "English");
}

TEST_CASE("test function2 options", "[function2]") {