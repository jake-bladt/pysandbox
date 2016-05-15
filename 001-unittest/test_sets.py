import unittest

class TestSets(unittest.TestCase):
  "Testing set functions"

  def test_dict_keys_as_set(self):
    stacks = {
      "Jake": 10785,
      "Mitch": 5555,
      "Natalie": 400,
      "Frannie": 6005 
    }

    self.assertTrue("Frannie" in set(stacks))


  def test_dict_values_as_set(self):
    hands = {
      "Jake": {'Ah', 'As'},
      "Mitch": {'Kh', 'Kc'},
      "Natalie": {'Ks', 'Qs'},
      "Frannie": {'Kd', 'Qd'} 
    }

    self.assertTrue('As' in hands['Jake'])

  def test_intersection(self):
    valid_users = { 'Thomas', 'Richard', 'Harold' }
    self.assertFalse(valid_users & {'Manish', 'Jake'})
    self.assertTrue(valid_users & {'Thomas', 'Jake'})
