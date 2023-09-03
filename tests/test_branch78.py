from functions.branch78 import branch78
import pytest

def test_branch78_positive_numbers():
  assert branch78(5, 3) == 2 

def test_branch78_equal_numbers():
  assert branch78(4, 4) == 16

def test_branch78_negative_numbers():
  assert branch78(-3, -2) == -5

def test_branch78_mixed_numbers():
  assert branch78(-3, 5) == -8 

def test_branch78_greater_number_first():
  assert branch78(10, 5) == 15

def test_branch78_greater_number_second():
  assert branch78(5, 10) == 15