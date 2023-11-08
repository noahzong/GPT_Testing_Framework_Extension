from functions.function8 import function8
import pytest

def test_function8_1():
    assert function8("hello", [1, 2, 3], True, 4, 5.2) == "hello4"
    
def test_function8_2():
    assert function8("world", [4, 5, 6], False, 7, 8.3) == "[4, 5, 6]8.3"