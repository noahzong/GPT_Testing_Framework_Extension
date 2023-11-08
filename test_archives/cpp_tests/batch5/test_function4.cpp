#include "../catch.hpp"
#include "../functions/function4.cpp"

TEST_CASE("Calculate final value", "[function4]") 
{
    function4 instance("John", 25, 'M', 15000);
    instance.list1 = {1, 2, 3};
    instance.list2 = {4, 5, 6};
    instance.dict1 = {{'a', 1}, {'b', 2}};
    instance.dict2 = {{'c', 3}, {'d', 4}};
    instance.str1 = "abc";
    instance.str2 = "def";
    instance.int1 = 5;
    instance.int2 = 10;
    instance.float1 = 1.2;
    instance.float2 = 3.4;
    instance.char1 = 'x';
    instance.char2 = 'y';
 
    REQUIRE(instance.calculate_final_value() == 276.6);
}