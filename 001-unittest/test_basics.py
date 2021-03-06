import unittest

import fact
import lists
import matrix

class TestBasics(unittest.TestCase):
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
    ls = lists.get_default_list()
    self.assertEqual(ls[-1], 13)	

  def test_list_replacement(self):
    ls = lists.get_default_list()
    ls[1] -= ls[0]
    self.assertEqual(ls[1], 1)

  def test_step(self):
    ls = lists.get_default_list()
    sl = ls[::2]
    self.assertEqual(sl[-1], ls[-2])

  def test_diffeomorphism(self):
    ls = lists.get_default_list()
    self.assertEqual(ls, ls[::-1][::-1])

  def test_append(self):
    ls = lists.get_default_list()
    old_len = len(ls)
    ls.append(17)
    self.assertEqual(old_len + 1, len(ls))

  def test_combine(self):
    ls1 = lists.get_default_list()
    ls2 = lists.get_next_list()
    ls1 += ls2
    self.assertEqual(10, len(ls1))

  def test_append_instead_of_combine(self):
    ls1 = lists.get_default_list()
    ls2 = lists.get_next_list()
    ls1.append(ls2)
    self.assertEqual(7, len(ls1))
    self.assertEqual(ls1[6][0], 17)

  def test_delete(self):
    ls1 = lists.get_default_list()
    del ls1[0]
    self.assertEqual(ls1[0], 3)

  def test_append_and_pop(self):
    ls = lists.get_default_list()
    ls.append(17)
    lifo = ls.pop()
    self.assertEqual(lifo, 17)
    self.assertEqual(ls, lists.get_default_list())

  def test_in(self):
    ls = lists.get_default_list()
    self.assertTrue(2 in ls)
    self.assertFalse(1 in ls)

  def test_join_split(self):
    ls = lists.get_house_list()
    div = ", "
    str = div.join(ls)
    self.assertEqual(str.split(div), ls)

  def test_tuple(self):
    t = 1,
    self.assertEqual((1,), t)

if __name__ == '__main__':
    unittest.main()
