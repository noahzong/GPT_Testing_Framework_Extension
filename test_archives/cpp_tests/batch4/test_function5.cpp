#include "../catch.hpp"
#include "../functions/function5.cpp"

TEST_CASE("function5 returns the correct result for test case 1", "[function5]") {
    std::string str1 = "test";
    std::string str2 = "string";
    int int1 = 5;
    int int2 = 10;
    float float1 = 5.5;
    float float2 = 2.2;
    bool bool1 = true;
    REQUIRE(function5(str1, str2, int1, int2, float1, float2, bool1) == "tg502.5True");
}

TEST_CASE("function5 returns the correct result for test case 2", "[function5]") {
    std::string str1 = "Hello";
    std::string str2 = "World";
    int int1 = 4;
    int int2 = 6;
    float float1 = 3.5;
    float float2 = 1.7;
    bool bool1 = false;
    REQUIRE(function5(str1,