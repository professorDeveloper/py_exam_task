from exam.number import Number


class User:
    def __init__(self, username, password, address):
        self.username = username
        self.password = password
        self.address = address
        self.__numbers = []  # Encapsulated attribute

    @property
    def numbers(self):  # Pythonic naming, simply 'numbers'
        return self.__numbers

    @numbers.setter
    def numbers(self, number):  # Same name as the property
        self.__numbers.append(number)  # Append a number to the list

    def to_dict(self):
        return {
            "username": self.username,
            "password": self.password,
            "address": self.address,
            "numbers": [number.to_dict() for number in self.__numbers]  # Serialize numbers
        }

    @staticmethod
    def from_dict(data):
        user = User(data['username'], data['password'], data['address'])
        if "numbers" in data:
            user.__numbers = [Number.from_dict(num) for num in data['numbers']]  # Deserialize numbers
        return user
