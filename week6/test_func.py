from demo_func import add
import pytest

# test case 1: second number is 0
def test_add_no1():
    a = 4
    b = 0
    c = add(a, b)
    assert c == 4

# test case 2: first number is 0
def test_add_no2():
    a = 0
    b = 4
    c = add(a, b)
    assert c == 4

# test case 3: both numbers are 0
def test_add_no3():
    a = 0
    b = 0
    c = add(a, b)
    assert c == 0