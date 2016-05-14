import unittest

import fact
import lists
import matrix

class TestPython(unittest.TestCase):
  "Testing basic concepts in Python"

  def setUp(self):
  	pass

  def tearDown(self):
  	pass

  def test_basic_addition(self):
  	self.assertEqual(2 + 2, 4)

  def test_factorial(self):
  	self.assertEqual(fact.factorial(5), 120)

  def test_matrix(self):
  	m = matrix.get_matrix()
  	self.assertEqual(m[1][1], 5)

  def test_list(self):
    l = lists.get_default_list()
    self.assertEqual(l[-1], 13)	

if __name__ == '__main__':
    unittest.main()
