from exam.number import Number


class User:
    __numbers: list[Number] = []
    def __init__(self, username, password,address):
        self.username = username
        self.address = address
        self.password = password
    @property
    def getNumbers(self):
        return self.__numbers

    @getNumbers.setter
    def setNumbers(self, number):
        self.__numbers.append(number)
