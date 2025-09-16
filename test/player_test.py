from functools import total_ordering

import unittest  # Import statement for unit test

import sys # Sys import for accessing app directory for test

import app.player

sys.path.insert(0,'../Source/Repo/SRUS-EK-Games-POR3/')
# Sys path insert for

from app.player import Player # Import statement for Player class

import random


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
        score_t = app.player.Player.scores
        return self, score_t

    def test_repr_return(self):
        repr_state = app.player.Player.__name__
        if repr_state == [Player(uid='01', name="Alice", score=10)]:
            return repr_state
        else:
            raise ValueError

    @total_ordering
    def test_sort_players(self):

        alice = Player(uid='01', name="Alice", score=10)
        bob = Player(uid='02', name="Bob", score=5)
        charlie = Player(uid='03', name="Charlie", score=15)

        self.assertTrue(alice > bob)
        self.assertTrue(alice < charlie)

        print(f' 1. comparing players:{alice > bob}')
        print(f' 2. comparing players:{alice < charlie}')
        print(f'Sorted_scores: {sorted([alice, bob, charlie])}')

    def test_sort_players_descending(self):

        players = [Player(uid='01', name="Alice", score=10), Player(uid='02', name="Bob", score=5),
                    Player(uid='03', name="Charlie", score=15)]

        manual_sort = [Player(uid='03', name="Charlie", score=15), Player(uid='01', name="Alice", score=10),
                          Player(uid='02', name="Bob", score=5)]

        sorted_players = Player.quick_sort(players.reverse)

        self.assertListEqual(sorted_players, manual_sort)

    def test_1000(self):

        players = [Player(f"Player {i}", uid=f"{i:03}", score=random.randint(0, 1000)) for i in range(1000)]

        sorted_players = Player.quick_sort(players)

        self.assertListEqual(players, sorted_players)
