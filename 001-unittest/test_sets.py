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

  def test_explicit_intersection(self):
    valid_users = { 'Thomas', 'Richard', 'Harold' }
    troublemakers = { 'Thomas', 'Jake', 'Mitch' }
    troublemaking_users = valid_users & troublemakers
    self.assertEqual(1, len(troublemaking_users))

  def test_union(self):
    valid_users = { 'Thomas', 'Richard', 'Harold' }
    troublemakers = { 'Thomas', 'Jake', 'Mitch' }
    set_of_all = valid_users | troublemakers;
    self.assertEqual(len(set_of_all), 5)

  def test_difference(self):
    valid_users = { 'Thomas', 'Richard', 'Harold' }
    troublemakers = { 'Thomas', 'Jake', 'Mitch' }
    users_in_good_standing = valid_users - troublemakers
    self.assertEqual(2, len(users_in_good_standing))
