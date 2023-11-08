#include "../catch.hpp"
#include "../functions/function6.cpp"

TEST_CASE("Test function6 with parameters 1, 'hello world', ['foo', 'bar']", "[function6]"){
  REQUIRE(function6(1, "hello world", std::vector<std::string>{"foo", "bar"}) == 6);
}

TEST_CASE("Test function6 with parameters 2, 'how are you', ['baz', 'qux']", "[function6]"){
  REQUIRE(function6(2, "how are you", std::vector<std::string>{"baz", "qux"}) == 8);
}