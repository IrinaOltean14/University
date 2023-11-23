
class As:
    def __init__(self, id, name, solution):
        self._id = id
        self._name = name
        self._solution = solution

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id):
        self._id = id

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, id):
        self._name = id

    @property
    def solution(self):
        return self._solution

    @solution.setter
    def solution(self, id):
        self._solution = id

    def __str__(self):
        return f"{self._id}, {self._name}, {self._solution}"


