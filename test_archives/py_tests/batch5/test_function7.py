from functions.function7 import function7
import pytest

def test_function7_init():
    f7 = function7(1, 2, 3)
    assert f7.user_input1 == 1
    assert f7.user_input2 == 2
    assert f7.user_input3 == 3
    assert f7.string1 == ""
    assert f7.list1 == []
    assert f7.int1 == 0
    assert f7.float1 == 0.0
    assert f7.dict1 == {}
    assert f7.boolean1 == False

def test_function7_method1():
    f7 = function7(1, 2, 3)
    f7.method1()
    assert f7.string1 == 3
    assert f7.list1 == [1, 2, 3]
    assert f7.int1 == 3
    assert f7.float1 == 1.5
    assert f7.dict1 == {1: 2, 2: 3}
    assert f7.boolean1 == True

