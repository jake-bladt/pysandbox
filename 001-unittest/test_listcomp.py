import unittest

class TestListComp(unittest.TestCase):
  "Tests of list comprehension"

  def test_basic_comp(self):
    x for x in range(1, 1000):
      self.assertLess(x, 1000)
