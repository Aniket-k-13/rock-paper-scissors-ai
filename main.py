# main.py

from RPS_game import play, quincy, abbey, kris, mrugesh
from RPS import player

# Play matches
play(player, quincy, 20, verbose=True)
play(player, abbey, 1000)
play(player, kris, 1000)
play(player, mrugesh, 1000)

# Uncomment below to run FCC tests
# import test_module
