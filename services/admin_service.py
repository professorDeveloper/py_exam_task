from share_data.share_data import user_file, numbers_file
from utils.file_utils import readListUser, readList, writeList
from models.models import Number
from share_data.share_data import admin


class AdminService:
    def __init__(self):
        self.users = readListUser(user_file)
        self.numbers = readList(numbers_file)
        self.admin = admin

    # Checker methods
    def checkNumberId(self, id: int):
        for number in self.numbers:
            if number.id == id:
                return True
            else:
                return False
        return False

    def checkNumber(self, id: str):
        for number in self.numbers:
            if number.number == id:
                return True
            else:
                return False
        return False

    def checkNumberFormat(self, number: str):  ## 50 R174QA
        if len(number) == 8:
            if (number[0].isdigit() and number[1].isdigit() and number[2].isalpha() and number[3].isdigit() and number[
                4].isdigit() and number[5].isdigit()
                    and number[6].isalpha() and number[7].isalpha()):
                return True
            else:
                return False
        else:
            return False

    # Getter Methods
    def getNumberById(self, id: int) -> Number:
        for number in self.numbers:
            if number.id == id:
                return number

    def findNumber(self, query) -> list[Number]:
        newList = []
        for number in self.numbers:
            if query in number.number:
                newList.append(number)
        return newList

    ## Number methods
    def numberList(self):
        if len(self.numbers) != 0:
            for number in self.numbers:
                if number.isSold:
                    print(
                        f"Id: {number.id} | Raqam: {number.number} | Narx: {number.price} | Sotilgan: {number.isSold} | Raqam egasi : {number.owner.username}")
                else:
                    print(
                        f"Id: {number.id} | Raqam: {number.number} | Narx: {number.price} | Sotilgan: {number.isSold}")
        else:
            print("Avto raqamlar ro'yxati bo'sh")

    def requestAddNumber(self):
        while True:
            print("Raqam faqat UZB formatida bo'lishi kerak")
            number = str(input("Raqamni kiriting: "))
            if self.checkNumberFormat(number):
                if self.checkNumber(number):
                    print("Bu raqam allaqachon mavjud")
                else:
                    price = int(input("Narxini kiriting: "))
                    if price < 0:
                        print("Narx 0 dan katta bo'lishi kerak")
                        continue
                    newNumber = Number(id=len(self.numbers) + 1, number=number, price=price)
                    self.numbers.append(newNumber)
                    writeList(self.numbers, numbers_file)
                    print("Raqam qo'shildi")
                    break
            else:
                print("Raqam xato formatda !")

    def delNumberByNumber(self, number: Number):
        sure = input("Raqamni o'chirmoqchimisiz ? (y/n): ")
        if sure == "y":
            carNumber = number
            self.numbers.remove(carNumber)
            writeList(self.numbers, numbers_file)
            print("Raqam o'chirildi")
        else:
            print("Raqam o'chirish bekor qilindi")

    def delNumber(self):
        self.numberList()
        delId = input("Raqam id ni kiriting: ")
        if delId.isdigit():
            if self.checkNumberId(int(delId)):
                carNumber = self.getNumberById(int(delId))
                if carNumber.isSold:
                    print("Sotilgan raqamlarda o'chirish mumkun emas !")
                else:
                    sure = input("Raqamni o'chirmoqchimisiz ? (y/n): ")
                    if sure == "y":
                        carNumber = self.getNumberById(int(delId))
                        self.numbers.remove(carNumber)
                        writeList(self.numbers, numbers_file)
                        print("Raqam o'chirildi")
                    else:
                        print("Raqam o'chirish bekor qilindi")
            else:
                print("Raqam mavjud emas")
        else:
            print("Raqam id ni xato formatda !")

    def editNumber(self):
        self.numberList()
        editId = input("Raqam id ni kiriting: ")
        if editId.isdigit():
            if self.checkNumberId(int(editId)):
                carNumber = self.getNumberById(int(editId))
                if carNumber.isSold:
                    print("Sotilgan raqamlarda o'zgartirish mumkun emas !")
                else:
                    newNumber = input("Yangi raqamni kiriting: ")
                    if self.checkNumber(newNumber):
                        print("Bu raqam allaqachon mavjud")
                    else:
                        newPrice = input("Yangi narxni kiriting: ")
                        if newPrice.isdigit():
                            newPrice = int(newPrice)
                            if newPrice < 0:
                                print("Narx 0 dan katta bo'lishi kerak")
                            else:
                                carNumber.number = newNumber
                                carNumber.price = newPrice
                                writeList(self.numbers, numbers_file)
                                print("Raqam tahrildi")
                        else:
                            print("Narx xato formatda !")
            else:
                print("Raqam mavjud emas")
        else:
            print("Raqam id ni xato formatda !")

    def editNumberByNumber(self, number: Number):
        while True:
            carNumber = number
            carNumberEdit = input(f"Raqamni o'zgartiring(xozirgi - {carNumber.number}): ")
            if self.checkNumberFormat(carNumberEdit):
                if self.checkNumber(carNumberEdit):
                    print("Bu raqam allaqachon mavjud")
                else:
                    priceEdit = input(f"Narxni o'zgartiring(xozirgi - {carNumber.price}): ")
                    if priceEdit.isdigit():
                        if int(priceEdit) < 0:
                            print("Narx 0 dan katta bo'lishi kerak")
                            continue
                        carNumber.price = priceEdit
                        carNumber.number = carNumberEdit
                        writeList(self.numbers, numbers_file)
                        print("Raqam malumotlari o'zgartirildi")
                        break
                    else:
                        print("Narx xato formatda !")
            else:
                print("Raqam xato formatda !")

    def soldNumberList(self):
        if len(self.numbers) != 0:
            filteredSoldNumbers = []
            for number in self.numbers:
                if number.isSold:
                    filteredSoldNumbers.append(number)
            if len(filteredSoldNumbers) != 0:
                for number in filteredSoldNumbers:
                    print(f"Raqam: {number.number} | Narx: {number.price} | Raqam egasi : {number.owner.username}")
            else:
                print("Sotilgan raqamlar ro'yxati bo'sh")
        else:
            print("Sotilgan raqamlar ro'yxati bo'sh")

    def searchNumber(self):
        if len(self.numbers) != 0:
            number = str(input("Raqamni kiriting: "))
            foundList = self.findNumber(number)
            if len(foundList) != 0:
                while True:
                    for number in foundList:
                        if number.isSold:
                            print(
                                f"Id: {number.id} | Raqam: {number.number} | Narx: {number.price} | Sotilgan: {number.isSold} | Raqam egasi : {self.users[number.owner].username}")
                        else:
                            print(
                                f"Id: {number.id} | Raqam: {number.number} | Narx: {number.price} | Sotilgan: {number.isSold}")
                    print("1-> Raqamni o`chirish")
                    print("2-> Raqamni o`zgartirish")
                    print("3-> Chiqish")
                    choice = input("Tanlash: ")
                    if choice == "1":
                        carNumId = input("Raqam id ni kiriting: ")
                        if carNumId.isdigit():
                            if self.checkNumberId(int(carNumId)):
                                carNumber = self.getNumberById(int(carNumId))
                                if carNumber.isSold:
                                    print("Sotilgan raqamlarda o'chirish mumkun emas")
                                else:
                                    self.delNumberByNumber(self.getNumberById(int(carNumId)))
                            else:
                                print("Raqam mavjud emas")
                        else:
                            print("Raqam id ni xato formatda !")

                    elif choice == "2":
                        carNumId = input("Raqam id ni kiriting: ")
                        if carNumId.isdigit():
                            if self.checkNumberId(int(carNumId)):
                                carNumber = self.getNumberById(int(carNumId))
                                if not carNumber.isSold:
                                    self.editNumberByNumber(self.getNumberById(int(carNumId)))
                                else:
                                    print("Sotilgan raqamlarda o'zgartirish mumkun emas")
                            else:
                                print("Raqam mavjud emas")
                        else:
                            print("Raqam id ni xato formatda !")

                    elif choice == "3":
                        break
                    else:
                        print("Xato tanlov")
            else:
                print("Raqam mavjud emas")
        else:
            print("Raqamlar ro'yxati bo'sh")

    ## User methods
    def userList(self):
        if len(self.users) != 0:
            for user in self.users:
                print(f"Username: {user.username} | Password: {user.password} | Address: {user.address}")
        else:
            print("Foydalanuvchilar ro'yxati bo'sh")

    def mostSoldUser(self):
        if len(self.numbers) != 0:
            filteredSoldNumbers = []
            for number in self.numbers:
                if number.isSold:
                    filteredSoldNumbers.append(number)
            if len(filteredSoldNumbers) != 0:
                mostSoldUser = max(filteredSoldNumbers, key=lambda x: x.owner)
                print(
                    f"Eng ko'p raqam sotib olgan foydalanuvchi: {self.users[mostSoldUser.owner].username} | Raqamlar soni: {len(filteredSoldNumbers)}")
            else:
                print("Sotilgan raqamlar ro'yxati bo'sh")
        else:
            print("Sotilgan raqamlar ro'yxati bo'sh")

    def loginAdmin(self):
        print("Admin paneliga xush kelibsiz")
        password = input("PinCode ni kiriting: ")
        if not password.isdigit():
            print("Login yoki parol xato !")
            return
        if int(password) == admin.pinCode:
            self.adminPanel()
        else:
            print("Login yoki parol xato !")

    ## Admin Panel

    def adminPanel(self):
        print("Admin paneliga xush kelibsiz")
        while True:
            print("1. Foydalanuvchilar ro'yxatini ko'rish")
            print("2. Avto raqamlarini ro`yhati")
            print("3. Avto raqamlarini qo'shish")
            print("4. Avto raqamlarini o'chirish")
            print("5. Avto raqamlarini tahrirlash")
            print("6. Sotilgan raqamlar ro`yhati")
            print("7. Avto Raqamni qidirish.")
            print("8. Eng ko`p raqam sotib olgan foydalanuvchi")
            print("9. Chiqish")
            choice = input("Tanlash: ")
            if choice == "1":
                self.userList()
            elif choice == "2":
                self.numberList()
            elif choice == "3":
                self.requestAddNumber()
            elif choice == "4":
                self.delNumber()
            elif choice == "5":
                self.editNumber()
            elif choice == "6":
                self.soldNumberList()
            elif choice == "7":
                self.searchNumber()
            elif choice == "8":
                self.mostSoldUser()
            elif choice == "9":
                break
