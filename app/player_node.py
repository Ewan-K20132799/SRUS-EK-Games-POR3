from player import Player


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
    root: Node | None
    _current_node: Node | None
    _length: int
    _value: None

    def __init__(self,
                 player,
                 value=list[int],
                 _next: Node | None = None):
        self._root = player
        self._value = value
        self.next = _next
        self._length = 0
        self._current_node = self._root

    def __len__(self):

        return self._length

    def head(self):
        return self.head

    def prev(self):
        return self._value

    def next_node(self):
        return self.next

    def current_node(self):
        return self._current_node

    def prev_node(self):
        return self.prev_node

    def __str__(self):
        return str(self.value)

    def __repr__(self):
        class_name = self.__class__.__name__
        return f"Player({self.uid}, {class_name}{self._value}, {self._value})"