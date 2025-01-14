# in user.py
class User:
    def __init__(self, username, password, address):
        self.username = username
        self.password = password
        self.address = address

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
        }

    @staticmethod
    def from_dict(data):
        user = User(data['username'], data['password'], data['address'])
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
            "owner": self.owner.to_dict() if self.owner else None  # Convert owner to dict
        }

    @staticmethod
    def from_dict(data):
        owner = User.from_dict(data['owner']) if data.get('owner') else None
        return Number(id=data['id'], number=data['number'], isSold=data['isSold'], price=data['price'], owner=owner)

# in admin.py
class Admin:
    def __init__(self, pinCode):
        self.pinCode = pinCode

    def to_dict(self):
        return {
            "pinCode": self.pinCode
        }

    @staticmethod
    def from_dict(data):
        return Admin(pinCode=data['pinCode'])
