import unittest

class TestDicts(unittest.TestCase):
  "Testing dictionary functions"

  def test_dict_conversion(self):
    ls = [['Yankees', 7], ['Red Sox', 0]]
    d = dict(ls)
    self.assertEqual(d['Yankees'], 7)
