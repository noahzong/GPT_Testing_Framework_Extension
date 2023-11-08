#include "../catch.hpp"
#include "../functions/function5.cpp"

TEST_CASE("test_process_data_1") {
    function5 test_class("hello", 5, 3.4, true);
    REQUIRE(test_class.process_data() == 56.0);
}

TEST_CASE("test_process_data_2") {
    function5 test_class("hello", 5, 3.4, true);
    test_class.input_string = "world";
    REQUIRE(test_class.process_data() == 56.0);
}