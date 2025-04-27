import pytest
import math
from Svetlikova_LR6_Methods_part_1 import modul,argument,user_input
#тест ввода 
@pytest.mark.parametrize("x,expected",[("2",True),("-1",True),("0",True),("",False),(",",False),("d1",False)])
def test_user_input(x,expected):
  assert user_input(x)==expected 
#тест модуля комплексного числа 
@pytest.mark.parametrize("a,b,expected",[(3,4,5),(0,4,4),(-1,-1,2**0.5)])
def test_modul(a,b,expected):
  assert modul(a,b)==expected
#тест аргумента комплексного числа 
@pytest.mark.parametrize("a,b,expected",[(1,1,(math.pi)/4),(-1,1,-(math.pi)/4+math.pi),\
 (-1,-1,(math.pi)/4-math.pi),(0,1,(math.pi)/2),(0,-1,-(math.pi)/2),(0,0,0.0)])#for argument
def test_argument(a,b,expected):
  assert argument(a,b)==expected
  