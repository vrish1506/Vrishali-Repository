#Content of PyTest.py 

import pytest
def func(x):
 return x+1

def test_answer(y):
  assert func(y) == 5
  print ('Test Pass')

print('Test Executed')

test_answer(4)
