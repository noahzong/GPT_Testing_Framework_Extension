from functions.function2 import function2
import pytest

@pytest.fixture
def function2_obj():
    return function2("John", 12, 4, "English")

def test_function2_name(function2_obj):
    assert function2_obj.name == "John"

def test_function2_age(function2_obj):
    assert function2_obj.age == 12

def test_function2_grade(function2_obj):
    assert function2_obj.grade == 4

def test_function2_language(function2_obj):
    assert function2_obj.language == "English"

def test_function2_options(function2_obj):
    function2_obj.set_options(True, False, True, False)
    assert function2_obj.option1 == True
    assert function2_obj.option2 == False
    assert function2_obj.option3 == True
    assert function2_obj.option4 == False

