
class PlayerNode:

    value: int
    next_node: Node | None

    def __init__(self,
                 value=int,
                 _next: Node | None = None):
        self._value = value
        self.