import unittest

class TestListComp(unittest.TestCase):
  "Tests of list comprehension"

  def test_basic_comp(self):
    all_nums = [x for x in range(1, 1000)]
    for num in all_nums:
      self.assertLess(num, 1000)
  
  def test_multivariate_comp(self):
    sets = [(op1, op2) for op1 in range(1,12) for op2 in range(1, 12)]
    for ops in sets:
      self.assertLess(ops[0] * ops[1], 144)
