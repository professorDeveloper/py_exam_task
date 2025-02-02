# in user.py
from datetime import datetime

class User:
    def __init__(self, username, password, address):
        self.username = username
        self.password = password
        self.address = address
        self.my_numbers = []  # Track purchased numbers

    def to_dict(self):
        return {
            "username": self.username,
            "password": self.password,
            "address": self.address,
            "my_numbers": [num.to_dict() for num in self.my_numbers],  # Include purchased numbers
        }

    @staticmethod
    def from_dict(data):
        user = User(data['username'], data['password'], data['address'])
        # Convert my_numbers from dict to Number objects
        user.my_numbers = [Number.from_dict(num) for num in data.get('my_numbers', [])]
        return user
    def checkLogin(self,username,password):
        return self.username == username and self.password == password

# in number.py
from datetime import datetime

# in number.py
class Number:
    def __init__(self, id, number, isSold=False, price=0, owner=None, date=None):
        self.__id = id
        self.number = number
        self.isSold = isSold
        self.price = price
        self.owner = owner
        self.date = date if date else datetime.now().strftime('%Y-%m-%d')  # Agar ko'rsatilmagan bo'lsa, standart sana ## 2024-01-15

    @property
    def id(self):
        return self.__id

    def checkId(self,id):
        return self.id == id

    def to_dict(self):
        return {
            "id": self.id,
            "number": self.number,
            "price": self.price,
            "isSold": self.isSold,
            "owner": self.owner if self.owner else None,  # Faqat egasining foydalanuvchi ismi
            "date": self.date,
        }

    @staticmethod
    def from_dict(data):
        if data['isSold']:
            owner =data['owner']
        else:
            owner = None
        return Number(id=data['id'], number=data['number'], isSold=data['isSold'], price=data['price'], owner=owner, date=data['date'])

# in admin.py
class Admin:
    def __init__(self, pinCode):
        self.pinCode = pinCode


