from functions.function8 import function8
import pytest
def test_function8_1():
    assert function8('Hello ', 10, [1, 2], True) == 'Hello 1210'

def test_function8_2():
    assert function8('Hi ', 15, [4, 5], False) == '4515'