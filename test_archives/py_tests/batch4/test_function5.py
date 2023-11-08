from functions.function5 import function5
import pytest

def test_function5_1():
    str1 = "test"
    str2 = "string"
    int1 = 5
    int2 = 10
    float1 = 5.5
    float2 = 2.2
    bool1 = True
    assert function5(str1, str2, int1, int2, float1, float2, bool1) == 'tg502.5True'

def test_function5_2():
    str1 = "Hello"
    str2 = "World"
    int1 = 4
    int2 = 6
    float1 = 3.5
    float2 = 1.7
    bool1 = False
    assert function5(str1, str2, int1, int2, float1, float2, bool1) == 'Hd242.058823529411765False'