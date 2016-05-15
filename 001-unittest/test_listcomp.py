import unittest

class TestListComp(unittest.TestCase):
  "Tests of list comprehension"

  def test_basic_comp(self):
    all_nums = [x for x in range(1, 1000)]
    for num in all_nums:
      self.assertLess(num, 1000)
