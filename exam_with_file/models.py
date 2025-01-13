# in user.py
class User:
    def __init__(self, username, password, address):
        self.username = username
        self.password = password
        self.address = address
        self.__numbers = []

    @property
    def numbers(self):
        return self.__numbers

    @numbers.setter
    def numbers(self, numbers):
        self.__numbers = numbers  # Allow setting a list of Number instances directly

    def to_dict(self):
        return {
            "username": self.username,
            "password": self.password,
            "address": self.address,
            "numbers": [n.to_dict() for n in self.__numbers]
        }

    @staticmethod
    def from_dict(data):
        user = User(data['username'], data['password'], data['address'])
        from exam.number import Number  # Import inside method to avoid circular imports
        user.numbers = [Number.from_dict(num) for num in data.get('numbers', [])]
        return user

# in number.py
class Number:
    def __init__(self, id, number, isSold=False, price=0, owner=None):
        self.id = id
        self.number = number
        self.isSold = isSold
        self.price = price
        self.owner = owner

    def to_dict(self):
        return {
            "id": self.id,
            "number": self.number,
            "price": self.price,
            "isSold": self.isSold,
            "owner": self.owner.username if self.owner else None
        }

    @staticmethod
    def from_dict(data):
        owner = User.from_dict(data['owner']) if data.get('owner') else None
        return Number(id=data['id'], number=data['number'], isSold=data['isSold'], price=data['price'], owner=owner)
