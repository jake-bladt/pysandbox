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
