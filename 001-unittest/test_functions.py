import unittest
import funcs

class TestFunctions(unittest.TestCase):
  "Test functions"

  def test_args(self):
    x = funcs.multiply(2, 5, 10, 15)
    self.assertEqual(x, 1500)
