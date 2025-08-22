from app.player_node import LinkedPlayerNode

class PlayerList: # Player list class

    def __init__(self,
                 value=None,
                 head=None): # init function for player list class
        self._head = None
        _head = head
        _value = value

        if _head is None:
            _head = LinkedPlayerNode()

    def is_empty(self):
       if LinkedPlayerNode() is self:
           return True
       return False

    def push_node(self, node): # Function to add node or head node
        if self._head:
            self.root = node
            self._head = node
            self.push_node(node)
            return self
        else:
            return LinkedPlayerNode() # Return node

    def pop_head_node(self, node):
        if self._head:
            self._next_node = self._head
            self._current_node = self._current_node.next_node
            self.pop_node(node)
            return self
        else:
            return LinkedPlayerNode()


    def push_tail_node(self, node):  # Function to add tail node
        if self._tail:
          self._next_node = self._tail
          self._current_node = node
          self.push_node(node)
          return self
        return LinkedPlayerNode()

    def pop_tail_node(self, node): # Function to delete tail node
        if self._tail:
            self._current_node = self._current_node.prev_node
            self._prev_node = self._tail
            self.LinkedPlayerNode.pop_node(node)
            return self


    def __repr__(self):
        class_name = self.__class__.__name__
        return f"Player({self.uid}, {class_name}{self._value}, {self._value})"


