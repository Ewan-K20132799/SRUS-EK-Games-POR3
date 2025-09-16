class Player:  # Player class

    def __init__(self,
                 uid: str,
                 name: str,
                 score: int):  # init function for unique identifier and name

        self._uid = uid  # private function for uid
        self._name = name  # private function for name
        self.score = score # private function for score

    def uid(self):
        return self._uid

    def name(self):
        return self._name

    def scores(self):
        if self.score < 0:
            raise ValueError
        else:
            return self.score

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
        return self.score

    def __set__(self, score: int):
        return self.score

    def __gt__(self, other):
        return self.score, other.score

    def __eq__(self, other):
        return self.score, other.score

    def __repr__(self):
        return f'name_{self.__class__.__name__}'

