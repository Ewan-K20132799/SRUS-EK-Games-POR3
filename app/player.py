class Player:  # Player class

    def __init__(self,
                 uid,
                 name,
                 score=int(0)):  # init function for unique identifier and name

        self._uid = uid  # private function for uid
        self._name = name  # private function for name
        self._score = score # private function for score

    def uid(self):
        return self._uid

    def name(self):
        return self._name

    def score(self):
        if self._score < 0:
            raise ValueError
        else:
            return self._score

    def __str__(self):  # String function for returning uid and name
        return self  # Returns the string of uid and name

    @classmethod
    def player_hash_function(cls, key: str) -> int:
        ...

    def __hash__(self):
        return self.player_hash_function(self.uid)

    def __eq__(self, other):
        return self.uid == other.uid

    def __get__(self, score: int):
        return self._score

    def __set__(self, score: int):
        return self._score

    def __repr__(self):
        self.__class__.__name__ = [Player('01', 'Alice', 10)]
        return self.__class__.__name__

