from functions.branch75 import branch75
import pytest

def test_branch75_option1():
    assert branch75(1) == "You chose option 1"

def test_branch75_option2():
    assert branch75(2) == "You chose option 2"

def test_branch75_option3():
    assert branch75(3) == "You chose option 3"

def test_branch75_option4():
    assert branch75(4) == "You chose option 4"

def test_branch75_option5():
    assert branch75(5) == "You chose option 5"

def test_branch75_option6():
    assert branch75(6) == "You chose option 6"

def test_branch75_option7():
    assert branch75(7) == "You chose option 7"

def test_branch75_option8():
    assert branch75(8) == "You chose option 8"

def test_branch75_option9():
    assert branch75(9) == "You chose option 9"

def test_branch75_option10():
    assert branch75(10) == "You chose option 10"

def test_branch75_invalid():
    assert branch75(-1) == "Invalid input"