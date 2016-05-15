import unittest
import funcs

class TestFunctions(unittest.TestCase):
  "Test functions"

  def test_args(self):
    x = funcs.multiply(2, 5, 10, 15)
    self.assertEqual(x, 1500)

  def test_kwargs(self):
    self.assertFalse(funcs.return_if_jake(jason = 'bladt'))
    self.assertEqual(funcs.return_if_jake(jake = 'bladt'), 'bladt')

  def test_call(self):
    self.assertEqual(42, funcs.call_with_42(funcs.multiply))
