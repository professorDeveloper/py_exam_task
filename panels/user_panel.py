from models.models import User
from utils.file_utils import writeList, readListUser, readList,  writeListUser


user_file = "users.json"
numbers_file = "numbers.json"


class UserPanel:
    def __init__(self):
        self.__users = readListUser(user_file)
        self.__numbers = readList(numbers_file)

    ## Checker Methods
    def checkNumberId(self, id: int):
        for number in self.__numbers:
            if number.checkId(id):
                return True
        return False

    def checkNotSoldNumberId(self, id: int):
        for number in self.__numbers:
            if number.checkId(id) and not number.isSold:
                return True
        return False

    def checkUserName(self, username):
        for user in self.__users:
            if user.username == username:
                return True
        return False

    def checkUserIsHave(self, username, password):
        for user in self.__users:
            if user.checkLogin(username,password):
                return True
        return False

    ## User Methods
    def getUser(self, username, password):
        for user in self.__users:
            if user.checkLogin(username,password):
                return user
        return None

    # Edit profile

    def updateUserNumbers(self,username,newUserName):
        for index in range(0, len(self.__numbers)):
            if self.__numbers[index].username == username:
                self.__numbers[index].username = newUserName

    def editProfile(self, user: User):
        username = input("Username: ")
        if not self.checkUserName(username):
            password = input("Password: ")
            address = input("Address: ")
            oldUserName =user.username
            newUserName = username
            self.updateUserNumbers(oldUserName,newUserName)
            user.username = username
            user.password = password
            user.address = address
            index = self.__users.index(user)
            self.__users[index] = user
            writeList(self.__users, user_file)
            print("Foydalanuvchi tahrirlandi !")
        else:
            print("Foydalanuvchi username mavjud !")

    # Number CRUD Methods
    def numberList(self):
        if len(self.__numbers) != 0:
            for number in self.__numbers:
                if not number.isSold:
                    print(
                        f"Id: {number.id} | Raqam: {number.number} | Narx: {number.price} | Sotilgan: {number.isSold}")
        else:
            print("Raqamlar ro'yxati bo'sh")

    def getNumberById(self, id: int):
        for number in self.__numbers:
            if number.checkId(id):
                return number
        return None

    def myNumber(self, user: User):
        if len(user.my_numbers) != 0:
            for number in user.my_numbers:
                print(f"Id: {number.id} | Raqam: {number.number} | Narx: {number.price} | Sotilgan: {number.isSold}")
        else:
            print("Sizda raqamlar mavjud emas")

    def buyNumber(self, user: User):
        self.__numbers =readList(numbers_file)
        soldNumbers = []
        for number in self.__numbers:
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
                        carIndex = self.__numbers.index(carNumber)
                        carNumber.isSold = True
                        carNumber.owner = user.username
                        self.__numbers[carIndex] = carNumber
                        user.my_numbers.append(carNumber)  # Add purchased number to my_numbers
                        writeList(self.__numbers, numbers_file)
                        writeListUser(self.__users, user_file)  # Save updated user data
                        print("Raqam sotib olindi !")
                    else:
                        print("Raqam sotish bekor qilindi")
                else:
                    print("Raqam mavjud emas")
            else:
                print("Raqam id ni xato formatda !")
        else:
            print("Sotilmagan Raqamlar ro'yxati bo'sh")

    def searchNumber(self):
        number = input("Raqamni kiriting: ")
        if number.isdigit():
            if self.checkNumberId(int(number)):
                for number in self.__numbers:
                    if number.number in number and number.isSold == False:
                        print(f"Id: {number.id} | Raqam: {number.number} | Narx: {number.price} ")
            else:
                print("Raqam mavjud emas")
        else:
            print("Raqam id ni xato formatda  !")

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
                self.searchNumber()
            elif choice == "7":
                sure = input("Chiqishni xohlaysizmi ? (y/n): ")
                if sure == "y":
                    break
                else:
                    print("Chiqish bekor qilindi")
            else:
                print("Xato tanlov !")

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
            self.__users.append(user)
            writeList(self.__users, user_file)
            self.userPanel(user)
        else:
            print("Foydalanuvchi login mavjud !")
