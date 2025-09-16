from functools import total_ordering


class Player:  # Player class

    def __init__(self,
                 uid: str,
                 name: str,
                 score: int):  # init function for unique identifier and name

        self.uid = uid  # private function for uid
        self.name = name  # private function for name
        self.score = score # private function for score

    def uid(self):
        return self.uid

    def name(self):
        return self.name

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

    def __get__(self, score: int):
        return self.score

    def __set__(self, score: int):
        return self.score

    @total_ordering
    def __gt__(self, other):
        return self.score > other.score

    def __eq__(self, other):
        return self.score == other.score

    def __repr__(self):
        return f'name_{self.name}'

    @classmethod
    def quick_sort(cls, array):
        if len(array) <= 1:
            return array
        pivot = array[0]
        left = []
        right = []
        for x in array[1:]:
            if x < pivot:
                left.append(x)
            else:
                right.append(x)
        return cls.quick_sort(left) + [pivot] + cls.quick_sort(right)
