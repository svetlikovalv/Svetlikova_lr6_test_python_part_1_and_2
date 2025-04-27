import pytest
from Svetlikova_LR6_Methods_part_2 import user_input,sum_of_digits,is_equal
#тест ввода 
@pytest.mark.parametrize("x,expected",\
    [("2",True),("-1",False),("0",True),\
 ("",False),(",",False),("d1",False),("a",False)])
def test_user_input(x,expected):
  assert user_input(x)==expected 
@pytest.mark.parametrize("num,expected",\
    [(105,6),(21,3),(0,0),(42,6),(35,8)])
def test_sum_of_digits(num,expected):
  assert sum_of_digits(num)==expected
@pytest.mark.parametrize("num1,num2,expected",\
    [(105,42,True),(21,35,False),(0,0,True),(99,88,False)])
def test_is_equal(num1,num2,expected):
  assert is_equal(num1,num2)==expected