from app.player_node import LinkedPlayerNode


def is_empty():
   if LinkedPlayerNode is None:
       return True
   else:
       return False


class PlayerList: # Player list class

    def __init__(self,
                 value=None,
                 head=None,
                 tail=None): # init function for player list class
        self._head = LinkedPlayerNode(head).node(head)
        self._tail = LinkedPlayerNode(tail).node(tail)
        _value = value

    def push_node(self, node): # Function to add node or head node
        if self._head:
            LinkedPlayerNode.root = node
            LinkedPlayerNode._head = node
            LinkedPlayerNode.push_node(self._head, node)
            return self
        else:
            return LinkedPlayerNode(self._head) # Return node

    def pop_head_node(self, node):
        if self._head:
            LinkedPlayerNode._next_node = self._head
            LinkedPlayerNode._current_node = LinkedPlayerNode._current_node.next_node
            LinkedPlayerNode.pop_node(node)
            return self
        else:
            return LinkedPlayerNode(self._head)


    def push_tail_node(self, node):  # Function to add tail node
        if self._tail:
          LinkedPlayerNode._next_node = self._tail
          LinkedPlayerNode._current_node = node
          LinkedPlayerNode.push_node(self._tail, node)
          return self
        return LinkedPlayerNode(self._tail)

    def pop_tail_node(self, node): # Function to delete tail node
        if self._tail:
            LinkedPlayerNode._current_node = LinkedPlayerNode._current_node.prev_node
            LinkedPlayerNode._prev_node = self._tail
            LinkedPlayerNode.pop_node(node)
            return self
        return LinkedPlayerNode(self._tail)



