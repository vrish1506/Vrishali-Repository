#content of TestClass.py

import pytest

class TestClass(object):
 def test1(self):
  x = "this" 
  assert 'h' in x 

 def test_two(self):
  x= "hello"
  assert hasattr(x,'check')

 def test_set_comparision():
  set1 = set("1308")
  set2 = set("8035")
  assert set1 == set2
  


