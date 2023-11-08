#include "../catch.hpp"
#include "../functions/function7.cpp"

TEST_CASE("Test function7 init") {
    Function7 f7 = Function7(1, 2, 3);
    REQUIRE(f7.user_input1 == 1);
    REQUIRE(f7.user_input2 == 2);
    REQUIRE(f7.user_input3 == 3);
    REQUIRE(f7.string1 == "");
    REQUIRE(f7.list1 == std::vector<int>{});
    REQUIRE(f7.int1 == 0);
    REQUIRE(f7.float1 == 0.0);
    REQUIRE(f7.dict1 == std::map<int, int>{});
    REQUIRE(f7.boolean1 == false);
}

TEST_CASE("Test function7 method1") {
    Function7 f7 = Function7(1, 2, 3);
    f7.method1();
    REQUIRE(f7.string1 == "3");
    REQUIRE(f7.