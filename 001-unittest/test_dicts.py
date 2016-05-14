import unittest

class TestDicts(unittest.TestCase):
  "Testing dictionary functions"

  def test_dict_conversion(self):
    ls = [['Yankees', 7], ['Red Sox', 0]]
    d = dict(ls)
    self.assertEqual(d['Yankees'], 7)

  def test_string_to_dict(self):
    cypher = ['an', 'bo', 'cp', 'dq']
    mapping = dict(cypher)
    self.assertEqual(mapping['d'], 'q')
