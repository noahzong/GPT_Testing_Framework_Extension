from functions.branch51 import branch51
import pytest
def test_branch51():
    assert branch51('A', 'B') == 'Result1'
    assert branch51('A', 'C') == 'Result2'
    assert branch51('A', 'D') == 'Result3'
    assert branch51('D', 'E') == 'Result4'
    assert branch51('D', 'F') == 'Result5'
    assert branch51('D', 'G') == 'Result6'
    assert branch51('X', 'Y') == 'Result7'