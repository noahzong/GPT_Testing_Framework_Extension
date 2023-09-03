from functions.branch39 import branch39
def test_branch39_num_str():
    assert branch39(1, "hello") == 6

def test_branch39_num_str_long():
    assert branch39(1, "testing") == 10

def test_branch39_num_nonstr():
    assert branch39(1, 5) == 6

def test_branch39_nonnum_str():
    assert branch39("hello", "testing") == 50

def test_branch39_nonnum_str_long():
    assert branch39("hello", "testinglong") == 100

def test_branch39_nonnum_nonstr():
    assert branch39(5, 10) == -5