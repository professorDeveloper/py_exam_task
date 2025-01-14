from models.models import User
from utils.file_utils import writeList, readListUser, readList
from share_data.share_data import user_file, numbers_file


class UserService:
    def __init__(self):
        self.users = readListUser(user_file)
        self.numbers = readList(numbers_file)

    ## Checker Medhods

    def checkNumberId(self, id: int):
        self.numbers = readList(numbers_file)
        for number in self.numbers:
            if number.id == id:
                return True

        return False

    def checkNotSoldNumberId(self, id: int):
        self.numbers = readList(numbers_file)
        for number in self.numbers:
            if number.id == id and not number.isSold:
                return True

        return False

    def checkUserName(self, username):
        for user in self.users:
            if user.username == username:
                return True
        return False

    def checkUserIsHave(self, username, password):  ## Foydalanuvchi mavjudligini tekshirish
        for user in self.users:  ## Foydalanuvchilar ro'yxatini olish
            if user.username == username and user.password == password:  ## Foydalanuvchini tekshirish
                return True
        return False

    ## User Methods

    def getUser(self, username, password):  ## Foydalanuvchini olish login va password orqali
        for user in self.users:
            if user.username == username and user.password == password:
                return user
        return None

    # Edit profile
    def editProfile(self, user: User):  ## Profile ni tahrirlash
        username = input("Username: ")
        if not self.checkUserName(username):  ## Foydalanuvchi login mavjud emasligini tekshirish
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

    # Number CRUD Methods  Get Numbers
    def numberList(self):
        self.numbers = readList(numbers_file)
        if len(self.numbers) != 0:
            for number in self.numbers:
                print(f"Id: {number.id} | Raqam: {number.number} | Narx: {number.price} | Sotilgan: {number.isSold}")
        else:
            print("Raqamlar ro'yxati bo'sh")

    def getNumberById(self, id: int):  ## Raqamni id orqali olish

        for number in self.numbers:
            if number.id == id:
                return number
        return None

    def myNumber(self, user: User):  ## Mening raqamlarim
        self.numbers = readList(numbers_file)  ## raqamlar ro'yxatini olish
        if len(self.numbers) != 0:  ## raqamlar mavjudligiga tekshirish
            for number in self.numbers:
                if number.isSold:
                    if number.owner.username == user.username:
                        print(
                            f"Id: {number.id} | Raqam: {number.number} | Narx: {number.price} | Sotilgan: {number.isSold}")
        else:
            print("Sizda raqamlar mavjud emas")

    def buyNumber(self, user: User):  ### User Raqam sotib olish qismi
        if len(self.numbers) != 0:  ## raqamlar mavjudlikga tekshirish
            soldNumbers = []  ## sotilmagan raqamlarni bitta qilib saqlash
            for number in self.numbers:
                if not number.isSold:
                    soldNumbers.append(number)
                    print(
                        f"Id: {number.id} | Raqam: {number.number} | Narx: {number.price} | Sotilgan: {number.isSold}")
            if len(soldNumbers) != 0:  ## Sotilmagan raqamlar mavjudligiga tekshirish
                choice = input("ID orqali tanlang: ")  ### sotilmagan raqam id
                if choice.isdigit():
                    if self.checkNotSoldNumberId(int(choice)):
                        sure = input("Raqamni sotib olishni xohlaysizmi ? (y/n): ")  ##  To`lovni tasdiqlash !
                        if sure == "y":
                            carNumber = self.getNumberById(int(choice))
                            carIndex = self.numbers.index(carNumber)
                            carNumber.isSold = True
                            carNumber.owner = user
                            self.numbers[carIndex] = carNumber
                            writeList(self.numbers,
                                      numbers_file)  ## Raqamni malumotlar bazasidan yangilash yani egasi raqam sotib olganligini belgilash
                            print("Raqam sotib olindi !")
                        else:
                            print("Raqam sotish bekor qilindi")  ## Raqam sotish bekor qilindi
                    else:
                        print("Raqam mavjud emas")


                else:
                    print("Raqam id ni xato formatda !")
            else:
                print(" Sotilmagan Raqamlar ro'yxati bo'sh")
        else:
            print("Raqamlar ro'yxati bo'sh")

    def searchNumber(self, user: User):  ## Raqamni qidirish
        number = input("Raqamni kiriting: ")  # raqamni qidirish
        if number.isdigit():  ## raqamni uzb formatga tekshirish
            if self.checkNumberId(int(number)):
                for number in self.numbers:
                    if number.number == number:  ## raqamni raqamlar ro'yxatiga tekshirish
                        print(
                            f"Id: {number.id} | Raqam: {number.number} | Narx: {number.price} | Sotilgan: {number.isSold}")
            else:
                print("Raqam mavjud emas")
        else:
            print("Raqam id ni xato formatda  (50R174QA)!")

    ## UserPanel
    def userPanel(self, user: User):
        print("Foydalanuvchi paneliga xush kelibsiz")
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
