import unittest
import fact

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

if __name__ == '__main__':
    unittest.main()
