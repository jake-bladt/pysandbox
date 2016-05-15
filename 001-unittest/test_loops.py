import unittest

import lists

class TestLoops(unittest.TestCase):
  "tests for loops and navigation"

  def test_for(self):
    for x in lists.get_default_list():
      self.assertGreater(x, 1)
