from functions.branch62 import branch62
import pytest

def test_positive_positive_inputs():
  assert branch62(2,3) == 26

def test_negative_negative_inputs():
  assert branch62(-2,-3) == -5

def test_positive_negative_inputs():
  assert branch62(2,-3) == -1

def test_zero_inputs():
  assert branch62(0,0) == 0

def test_positive_zero_input():
  assert branch62(2,0) == 10

def test_negative_zero_input():
  assert branch62(-2,0) == -10

def test_zero_positive_input():
  assert branch62(0,2) == 10

def test_zero_negative_input():
  assert branch62(0,-2) == -20

def test_positive_positive_output2():
  assert branch62(2,3) == 26

def test_negative_negative_output2():
  assert branch62(-2,-3) == -15

def test_positive_negative_output2():
  assert branch62(2,-3) == 11

def test_zero_inputs_output2():
  assert branch62(0,0) == 10

def test_positive_zero_input_output2():
  assert branch62(2,0) == 10

def test_negative_zero_input_output2():
  assert branch62(-2,0) == -10

def test_zero_positive_input_output2():
  assert branch62(0,2) == 20

def test_zero_negative_input_output2():
  assert branch62(0,-2) == -10