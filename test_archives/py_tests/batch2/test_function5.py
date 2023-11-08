from functions.function5 import function5
import pytest

def test_function5_1():
    assert function5(4, 5.2, "hello", ["a", "b", "c"]) == (9.2, ["helloa", "hellob", "helloc"])

def test_function5_2():
    assert function5(2, 3.3, "world", ["d", "e"]) == (5.3, ["worldd", "worlde"])