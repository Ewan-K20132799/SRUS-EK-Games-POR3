from __future__ import annotations

from player import Player





class PlayerNode:

    Node: None
    value: int
    next_node: Node 

    def __init__(self,
                 player,
                 value=int,
                 _next: next_node = None
                 ) -> None:
        self.Player = Player
        self._player = player
        self._value = value
        self.next = _next

    @property
    def value(self):
        return Player

    @value.setter
    def value(self, value):
        self._value = value

    def key_uid(self):
        player = Player.uid
        return player

    def __str__(self):
        return str(self.value)

    def __repr__(self):
        class_name = self.__class__.__name__
        return f"Player({self.Player.uid}, {class_name}{self.Player.name}, {self._value})"


class LinkedPlayerNode:
    Node: None
    node: Node
    root: Node
    _current_node: Node
    _next_node: Node
    _prev_node: Node
    _length: int
    _value: None
    _head: None 
    _next: None 
    _prev: None 
    _tail: None 
    

    def __init__(self,
                 player,
                 value=list[int],
                 _next: Node = None,
                 ) -> None:
        self.Player = Player
        self._root = player
        self._value = None
        self.next = _next
        self._length = len(value)
        self._current_node = self._root
        self._head = None
        self._next = None
        self._prev = None
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

    def push_node(self, node): # Function to add node or head node
        if self._head:
            self.root = node
        self._current_node = node
        self._length += 1
        return self

    def push_tail_node(self, node): # Function to add tail node
        if self._tail:
            self._next_node = self._tail
        self._current_node = node
        self._length += 1
        return self

    def pop_node(self): # Function to delete node or head node
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
            self._prev_node = self._tail
            self._length -= 1
            return self._tail
        self._current_node = self._current_node.prev_node
        self._length -= 1
        return self

    def __str__(self):
        return str(self._value)

    def __repr__(self):
        class_name = self.__class__.__name__
        return f"Player({self.Player.uid}, {class_name}{self.Player.name}, {self._value})"

    if __name__ == "__main__":
        pass
