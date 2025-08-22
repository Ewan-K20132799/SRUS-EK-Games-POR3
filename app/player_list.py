from app.player_node import LinkedPlayerNode

class PlayerList: # Player list class

    def __init__(self,
                 value=None,
                 headp=None): # init function for player list class
        _headp = headp
        _value = value

        if _headp is None:
            _headp = LinkedPlayerNode()

    def is_empty(self):
       if LinkedPlayerNode() is self:
           return True
       return False

    def __repr__(self):
        class_name = self.__class__.__name__
        return f"Player({self.uid}, {class_name}{self._value}, {self._value})"


