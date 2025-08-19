from player import Player
class PlayerNode:

    value: int
    next_node: None
    Node: None

    def __init__(self,
                 value=int,
                 _next: Node | None = None):
        self._value = value
        self.next = _next

    @property
    def value(self):
        return(Player)

    def __str__(self):
        return str(self.value)
