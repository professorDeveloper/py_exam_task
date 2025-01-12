from exam.share_data import user_list
from exam.user import User
from exam.number import Number
from exam.share_data import numbers_list


class UserService:

    def checkUserIsHave(self, username, password):
        for user in user_list:
            if user.username == username and user.password == password:
                return True
        return False

    def checkNumberIsHave(self, number: str):
        if number in [number.number for number in numbers_list]:
            return True
        else:
            return False

    def checkIdIsHave(self, id: int):
        for number in numbers_list:
            if number.id == id:
                return True
            else:
                return False
        return False

    def getUser(self, username, password):
        for user in user_list:
            if user.username == username and user.password == password:
                return user

    def checkUserName(self, username):
        for user in user_list:
            if user.username == username:
                return True
        return False

    def numberList(self):
        if len(numbers_list) != 0:
            for number in numbers_list:
                print(f"Id: {number.id} | Raqam: {number.number} | Narx: {number.price} | Sotilgan: {number.isSold}")
        else:
            print("Raqamlar ro'yxati bo'sh")

    def checkIsSold(self):
        for number in numbers_list:
            if number.isSold:
                return True
        return False

    def myNumber(self, user: User):
        if self.checkIsSold():
            for number in numbers_list:
                if number.owner.username == user.username:
                    print(
                        f"Id: {number.id} | Raqam: {number.number} | Narx: {number.price} | Sotilgan: {number.isSold}")
        else:
            print("Sizda raqamlar mavjud emas")

    def getNumberById(self, id: int) -> Number:
        for number in numbers_list:
            if number.id == id:
                return number

    def buyNumber(self, user: User):
        for number in numbers_list:
            if number.owner.username != user.username and not number.isSold:
                print(f"Id: {number.id} | Raqam: {number.number} | Narx: {number.price}")
        choice = input("avtomobil raqamini tanlang: ")
        if choice.isdigit():
            if self.checkIdIsHave(int(choice)):
                sure = input("Raqamni sotib olishni xohlaysizmi ? (ha/yo'q): ")
                if sure == "ha":
                    carNumber = self.getNumberById(int(choice))
                    carNumber.isSold = True
                    carNumber.owner = user
                    print("Raqam sotib olindi !")
                else:
                    print("Raqam sotish bekor qilindi")

    def userLogin(self):
        login = input("Login: ")
        password = input("Password: ")
        if self.checkUserIsHave(login, password):
            self.userPanel(self.getUser(login, password))
        else:
            print("Foydalanuvchi mavjud emas")

    def editProfile(self, user: User):
        username = input("Username: ")
        if not self.checkUserName(username):
            password = input("Password: ")
            address = input("Address: ")
            user.username = username
            user.password = password
            user.address = address
            indexus = user_list.index(user)
            user_list[indexus] = user
        else:
            print("Foydalanuvchi username mavjud !")

    def userRegister(self):
        username = input("Username: ")
        if not self.checkUserName(username):
            password = input("Password: ")
            address = input("Address: ")
            user = User(username, password, address)
            user_list.append(user)
            self.userPanel(user)
        else:
            print("Foydalanuvchi username mavjud !")

    def searchNumber(self, user: User):
        number = input("Raqamni kiriting: ")
        if self.checkNumberIsHave(number):
            for number in numbers_list:
                if number.number == number:
                    print(
                        f"Id: {number.id} | Raqam: {number.number} | Narx: {number.price} | Sotilgan: {number.isSold}")
        else:
            print("Raqam mavjud emas")

    def userPanel(self, user: User):
        print("Foydalanuvchi paneliga xush kelibsiz")
        while True:
            print("1.Profil")
            print("2.Raqamlar ro`yhati")
            print("3.Mening raqamlarim")
            print("4.Raqam sotib olish")
            print("5.Profil tahrirlash")
            print("6.Raqamni qidirish")
            print("7.Chiqish")
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
                break
