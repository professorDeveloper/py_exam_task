from models.models import User
from utils.file_utils import writeList, readListUser, readList, updateUserNumbers, writeListUser
from share_data.share_data import user_file, numbers_file


class UserService:
    def __init__(self):
        self.users = readListUser(user_file)
        self.numbers = readList(numbers_file)

    ## Checker Methods
    def checkNumberId(self, id: int):
        for number in self.numbers:
            if number.id == id:
                return True
        return False

    def checkNotSoldNumberId(self, id: int):
        for number in self.numbers:
            if number.id == id and not number.isSold:
                return True
        return False

    def checkUserName(self, username):
        for user in self.users:
            if user.username == username:
                return True
        return False

    def checkUserIsHave(self, username, password):
        for user in self.users:
            if user.username == username and user.password == password:
                return True
        return False

    ## User Methods
    def getUser(self, username, password):
        for user in self.users:
            if user.username == username and user.password == password:
                return user
        return None

    # Edit profile
    def editProfile(self, user: User):
        username = input("Username: ")
        if not self.checkUserName(username):
            password = input("Password: ")
            address = input("Address: ")
            user.username = username
            user.password = password
            user.address = address
            index = self.users.index(user)
            self.users[index] = user
            writeList(self.users, user_file)
            print("Foydalanuvchi tahrirlandi !")
        else:
            print("Foydalanuvchi username mavjud !")

    # Number CRUD Methods
    def numberList(self):
        if len(self.numbers) != 0:
            for number in self.numbers:
                print(f"Id: {number.id} | Raqam: {number.number} | Narx: {number.price} | Sotilgan: {number.isSold}")
        else:
            print("Raqamlar ro'yxati bo'sh")

    def getNumberById(self, id: int):
        for number in self.numbers:
            if number.id == id:
                return number
        return None

    def myNumber(self, user: User):
        if len(user.my_numbers) != 0:
            for number in user.my_numbers:
                print(f"Id: {number.id} | Raqam: {number.number} | Narx: {number.price} | Sotilgan: {number.isSold}")
        else:
            print("Sizda raqamlar mavjud emas")

    def buyNumber(self, user: User):
        self.numbers =readList(numbers_file)
        soldNumbers = []
        for number in self.numbers:
            if not number.isSold:
                soldNumbers.append(number)
                print(f"Id: {number.id} | Raqam: {number.number} | Narx: {number.price} | Sotilgan: {number.isSold}")
        if len(soldNumbers) != 0:
            choice = input("ID orqali tanlang: ")
            if choice.isdigit():
                if self.checkNotSoldNumberId(int(choice)):
                    sure = input("Raqamni sotib olishni xohlaysizmi ? (y/n): ")
                    if sure == "y":
                        carNumber = self.getNumberById(int(choice))
                        carIndex = self.numbers.index(carNumber)
                        carNumber.isSold = True
                        carNumber.owner = user.username
                        self.numbers[carIndex] = carNumber
                        user.my_numbers.append(carNumber)  # Add purchased number to my_numbers
                        writeList(self.numbers, numbers_file)
                        writeListUser(self.users, user_file)  # Save updated user data
                        print("Raqam sotib olindi !")
                    else:
                        print("Raqam sotish bekor qilindi")
                else:
                    print("Raqam mavjud emas")
            else:
                print("Raqam id ni xato formatda !")
        else:
            print("Sotilmagan Raqamlar ro'yxati bo'sh")

    def searchNumber(self, user: User):
        number = input("Raqamni kiriting: ")
        if number.isdigit():
            if self.checkNumberId(int(number)):
                for number in self.numbers:
                    if number.number == number:
                        print(f"Id: {number.id} | Raqam: {number.number} | Narx: {number.price} | Sotilgan: {number.isSold}")
            else:
                print("Raqam mavjud emas")
        else:
            print("Raqam id ni xato formatda  (50R174QA)!")

    def userPanel(self, user: User):
        while True:
            print("------------------------------------------------------------------")
            print("1.Profil")
            print("2.Raqamlar ro`yhati")
            print("3.Mening raqamlarim")
            print("4.Raqam sotib olish")
            print("5.Profil tahrirlash")
            print("6.Raqamni qidirish")
            print("7.Chiqish")
            print("------------------------------------------------------------------")
            choice = input("Tanlash: ")
            if choice == "1":
                print(f"Username: {user.username} | Password: {user.password} | Address: {user.address}")
            elif choice == "2":
                self.numberList()
            elif choice == "3":
                self.myNumber(user)
            elif choice == "4":
                self.buyNumber(user)
            elif choice == "5":
                self.editProfile(user)
            elif choice == "6":
                self.searchNumber(user)
            elif choice == "7":
                sure = input("Chiqishni xohlaysizmi ? (y/n): ")
                if sure == "y":
                    break
                else:
                    print("Chiqish bekor qilindi")

    def userLogin(self):
        login = input("Login: ")
        password = input("Password: ")
        if self.checkUserIsHave(login, password):
            self.userPanel(self.getUser(login, password))
        else:
            print("Foydalanuvchi mavjud emas")

    def userRegister(self):
        username = input("Login: ")
        if not self.checkUserName(username):
            password = input("Password: ")
            address = input("Address: ")
            user = User(username, password, address)
            self.users.append(user)
            writeList(self.users, user_file)
            self.userPanel(user)
        else:
            print("Foydalanuvchi login mavjud !")
