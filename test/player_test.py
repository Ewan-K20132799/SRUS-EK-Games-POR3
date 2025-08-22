import unittest  # Import statement for unit test

import sys

sys.path.insert(0,'../Source/Repo/SRUS-EK-Games/SRUS-EK-Games/')

from app.player import Player # Import statement for Player class

class TestPlayer(unittest.TestCase):  # Test class for player.py module

    def test_uid_returns_str(self):  # Tests property from Player class
        uid_t = Player(uid=str)  # uid_t is equal to uid in Player class
        self.assertEqual(self, uid_t)  # Assertion that uid from Player class is a string

    def test_name_returns_str(self):  # Tests property from Player class
        name_t = Player(name=str)  # name_t is equal to name in Player class
        self.assertEqual(self, name_t)  # Assertion that name from Player class is a string
