class Player:  # Player class

    def __init__(self,
                 uid=str,
                 name=str):  # init function for unique identifier and name
        self._uid = uid  # private function for uid
        self._name = name  # private function for name

    def __str__(self):  # String function for returning uid and name
        return self  # Returns the string of uid and name
