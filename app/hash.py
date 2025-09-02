from app.player import Player
from app.player_list import PlayerList
from app.player_node import PlayerNode


class PlayerHashMap:   # initiation of hash map class
    SIZE: int = 10
    def __init__(self, key: str | Player):
        self.hashmap = [PlayerList(key.uid)] % self.SIZE


    def __hash__(self):

        return




    def __getitem__(self, key: str | Player) -> int:
        if isinstance(key.uid, PlayerNode):
            return hash(key.uid) % self.SIZE
        else:
            return Player.player_hash_function(key) % self.SIZE





    def __setitem__(self,
                    key: str,
                    name: str,
                    changed_n: str,
                    index: str | Player) -> None:


        if key in index:
            _name = changed_n
            return
        else:
            _name = name
            return


    def __len__(self, key: str) -> int:
        pass


    def delete_item(self, key: str | Player, name: str):
        if isinstance(key.uid, PlayerNode):














    def display(self,
                key: str,
                name: str | Player) -> int:



