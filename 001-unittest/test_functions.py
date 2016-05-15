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

  def test_call_plus(self):
    product = funcs.call_with_42_and_more(funcs.multiply, 10, 10)
    self.assertEqual(product, 4200)

  def test_closure(self):
    fwater = funcs.get_water_function()
    fruit = fwater('melon')
    self.assertEqual(fruit, 'watermelon')

  def test_call_lambda(self):
    multiply_by_42 = lambda x: 42 * x
    self.assertEqual(420, multiply_by_42(10))

  def test_iterate_funcs(self):
    sum, diff, product, quotient = funcs.run_transformations(10, 5, \
      lambda x, y: x + y, lambda x, y: x - y, lambda x, y: x * y, lambda x, y: x / y)
    self.assertEqual(sum, 15)
    self.assertEqual(diff, 5)
    self.assertEqual(product, 50)
    self.assertEqual(quotient, 2)

  def test_function_generation(self):
    multipliers = funcs.get_multipliers(0, 5)
    self.assertEqual(multipliers[4](5), 20)
