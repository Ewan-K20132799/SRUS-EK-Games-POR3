import unittest  # Import statement for unit test

import sys # Sys import for accessing app directory for test

sys.path.insert(0,'../Source/Repo/SRUS-EK-Games/SRUS-EK-Games/')
# Sys path insert for

from app.player import Player # Import statement for Player class

import app.player_list # Import statement for player list

import app.player_node # Import

class PlayerListTest(unittest.TestCase):

    def test_is_empty(self):
        if app.player_node.LinkedPlayerNode() is self:
            return True
        return False

    def test_is_not_empty(self):
        if app.player_node.LinkedPlayerNode() is not self:
            return True
        return False




