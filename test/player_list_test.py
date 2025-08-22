import unittest  # Import statement for unit test

import sys # Sys import for accessing app directory for test

sys.path.insert(0,'../Source/Repo/SRUS-EK-Games/SRUS-EK-Games/')
# Sys path insert for

import app.player  # Import statement for Player class

import app.player_list # Import statement for player list

import app.player_node # Import statement for player node

class PlayerListTest(unittest.TestCase):

    def test_is_empty(self):
        if app.player_node.LinkedPlayerNode is self:
            return True
        return False

    def test_is_not_empty(self):
        if app.player_node.LinkedPlayerNode is not self:
            return True
        return False

    def test_next_node(self):
        if app.player_node.LinkedPlayerNode is self:
            return app.player_node.LinkedPlayerNode.next_node()
        else:
            return 0

    def test_prev(self):
        if app.player_node.LinkedPlayerNode is self:
            return app.player_node.LinkedPlayerNode.prev_node()
        else:
            return 0

    def test_push(self):
        if app.player_node.LinkedPlayerNode is self:
            return app.player_node.LinkedPlayerNode.push_node()
        else:
            return 0

    def test_pop(self):
        if app.player_node.LinkedPlayerNode is self:
            return app.player_node.LinkedPlayerNode.pop_node()
        else:
            return 0

    def test_display(self, forward):
        if display is