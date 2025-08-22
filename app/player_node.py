from __future__ import annotations

from poetry.console.commands import self

from player import Player

from typing import Any, Iterator

def key_uid(Player):
    player = Player
    return player.uid


class PlayerNode:

    Node: None
    value: int
    next_node: Node | None

    def __init__(self,
                 player,
                 value=int,
                 _next: Node | None = None
                 ) -> None:
        self._player = player
        self._value = value
        self.next = _next

    @property
    def value(self):
        return Player

    @value.setter
    def value(self, value):
        self._value = value

    @key_uid
    def uid(self):
        return Player.uid

    def __str__(self):
        return str(self.value)

    def __repr__(self):
        class_name = self.__class__.__name__
        return f"Player({self.uid}, {class_name}{self._value}, {self._value})"


class LinkedPlayerNode:
    Node: None
    node: Node
    root: Node
    _current_node: Node
    _next_node: Node
    _prev_node: Node
    _length: int
    _value: None
    _head: None | LinkedPlayerNode
    _next: None | LinkedPlayerNode
    _tail: None | LinkedPlayerNode


    def __init__(self,
                 player,
                 value=list[int],
                 _next: Node | None = None
                 ) -> None:
        self._root = player
        self._value = value
        self.next = _next
        self._length = len(value)
        self._current_node = self._root
        self._head = None
        self._next = None
        self._tail = None

    def __len__(self):

        return self._length

    def head(self):
        return self.head

    def prev_node(self):
        return self.prev_node

    def next_node(self):
        return self.next

    def current_node(self):
        return self._current_node

    def tail_node(self):
        return self.tail_node

    def push_node(self, node): # Function to add node
        if self._head:
            self.root = node
        self._current_node = node
        self._length += 1
        return self

    def push_tail_node(self, node): # Function to add tail node
        if self._tail:
            self.next_node = self._tail
        self._current_node = node
        self._length += 1
        return self

    def pop_node(self): # Function to delete node
        if self._head:
            self._next_node = self._head
            self._current_node = self._current_node.next_node
            self._length -= 1
            return self._head
        self._current_node = self._current_node.next_node
        self._length -= 1
        return self

    def pop_tail_node(self): # Function to delete tail node
        if self._tail:
            self._current_node = self._current_node.prev_node
            self.prev_node = self._tail
            self._length -= 1
            return self._tail
        self._current_node = self._current_node.prev_node
        self._length -= 1
        return self

    def __str__(self):
        return str(self.value)

    def __repr__(self):
        class_name = self.__class__.__name__
        return f"Player({self.uid}, {class_name}{self._value}, {self._value})"

    if __name__ == "__main__":
        pass
