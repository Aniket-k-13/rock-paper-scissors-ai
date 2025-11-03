# test_module.py

import unittest
from RPS_game import play, quincy, abbey, kris, mrugesh
from RPS import player

class RPS_Test(unittest.TestCase):
    def test_quincy(self):
        self.assertGreater(play(player, quincy, 1000), 0.6)
    def test_abbey(self):
        self.assertGreater(play(player, abbey, 1000), 0.6)
    def test_kris(self):
        self.assertGreater(play(player, kris, 1000), 0.6)
    def test_mrugesh(self):
        self.assertGreater(play(player, mrugesh, 1000), 0.6)

if __name__ == "__main__":
    unittest.main()
