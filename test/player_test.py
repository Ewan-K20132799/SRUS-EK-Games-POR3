import unittest  # Import statement for unit test

import sys # Sys import for accessing app directory for test

import app.player

sys.path.insert(0,'../Source/Repo/SRUS-EK-Games-POR3/')
# Sys path insert for

from app.player import Player # Import statement for Player class


class TestPlayer(unittest.TestCase):  # Test class for player.py module

    def test_uid_returns_str(self):  # Tests property from Player class
        uid_t = app.player.Player.uid  # uid_t is equal to uid in Player class
        return self, uid_t  # Assertion that uid from Player class is a string

    def test_name_returns_str(self):  # Tests property from Player class
        name_t = app.player.Player.name  # name_t is equal to name in Player class
        return self, name_t  # Assertion that name from Player class is a string

    def test_get_score(self):
        get = app.player.Player.__get__
        if get != int:
            assert ValueError
        else:
            assert get == int

    def test_set_score(self):
        set = app.player.Player.__set__
        if set != int:
            raise ValueError
        else:
            assert set == int

    def test_score_returns_int(self):
        score_t = app.player.Player.score
        return self, score_t

    def test_repr_return(self):
        repr_state = app.player.Player.__name__
        if repr_state == [Player('01', "Alice", 10)]:
            return repr_state
        else:
            raise ValueError

    def test_sort_players(self):
        alice = Player('01', "Alice", 10)
        bob = Player('02', "Bob", 5)

        self.assertGreater(alice, bob)