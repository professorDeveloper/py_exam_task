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
