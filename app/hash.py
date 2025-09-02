import player_node
from app.player import Player
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


