from app.player_node import LinkedPlayerNode
from app.player import Player

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

    def display(self, forward):
        if forward (self._head and self._tail):
            return self._head.display(forward)
        else:
            return self._tail.display(forward)

class PlayerHashMap:   # initiation of hash map class
    SIZE: int = 10
    def __init__(self, key: str | Player):
        self.hashmap = [PlayerList(key)] % self.SIZE


    def __hash__(self):

        return




    def __getitem__(self, key: str | Player) -> int:
        if isinstance(key, Player):
            return hash(key) % self.SIZE
        else:
            return Player.player_hash_function(key) % self.SIZE





    def __setitem__(self,
                    key: str,
                    name: str,
                    index: str | Player) -> None:


        if key in index:
            _name = ""
            return
        else:

            _name = ""
            return


    def __len__(self, key: str) -> int:








    def __delitem__(self, key: str, name: str):









    def display(self,
                key: str,
                name: str | Player) -> int:


