import unittest

import lists

class TestLoops(unittest.TestCase):
  "tests for loops and navigation"

  def test_for(self):
    for x in lists.get_default_list():
      self.assertGreater(x, 1)

  def test_iterate_key_values(self):
    mastery_levels = {
      65: 80,
      75: 90,
      90: 100
    }

    for near_mastery, mastery in mastery_levels.items():
      self.assertLess(near_mastery, mastery)

  def test_zip_to_dict(self):
    players = ['Jake', 'Mitch', 'Frannie', 'Natalie']
    stacks = [10000, 10000, 10000, 10000]
    player_stacks = dict(zip(players, stacks))
    for stack_size in player_stacks.values():
      self.assertEqual(stack_size, 10000)
