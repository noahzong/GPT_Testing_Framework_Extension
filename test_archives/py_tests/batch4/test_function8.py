from functions.function8 import function8
def test_function8_1():
    assert function8(3,5,"The answer is ",[1,2,3]) == ("The answer is 15", [4,5,6])

def test_function8_2():
    assert function8(2,6,"The answer is ",[4,5,6]) == ("The answer is 12", [6,7,8])