class Candidate:
    def __init__(self, surname, votes):
        self.surname = surname
        self.__votes = votes

    @property
    def votes(self):
        return self.__votes

    @votes.setter
    def votes(self, value):
        if value < 0:
            raise ValueError("Votes cannot be negative.")
        self.__votes = value