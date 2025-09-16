class Player:  # Player class

    def __init__(self,
                 uid=str,
                 name=str):  # init function for unique identifier and name
        self._uid = uid  # private function for uid
        self._name = name  # private function for name

    def uid(self):
        return self._uid

    def name(self):
        return self._name

    def score(self):


    def __str__(self):  # String function for returning uid and name
        return self  # Returns the string of uid and name

    @classmethod
    def player_hash_function(cls, key: str) -> int:
        ...

    def __hash__(self):
        return self.player_hash_function(self.uid)

    def __eq__(self, other):
        return self.uid == other.uid
