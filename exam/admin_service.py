from itertools import count

from exam.user import User
from exam.number import Number
from exam.share_data import user_list
from exam.share_data import admin
from exam.share_data import numbers_list


class AdminService():

    def userList(self):
        if len(user_list) != 0:
            for user in user_list:
                print(f"Username: {user.username} | Password: {user.password} | Address: {user.address}")
        else:
            print("Foydalanuvchilar ro'yxati bo'sh")

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

    def numberList(self):
        if len(numbers_list) != 0:
            for number in numbers_list:
                print(f"Id: {number.id} | Raqam: {number.number} | Narx: {number.price} | isSold: {number.isSold}")
        else:
            print("Raqamlar ro'yxati bo'sh")


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

    def getNumberById(self, id: int) -> Number:
        for number in numbers_list:
            if number.id == id:
                return number

    def requestAddNumber(self):
        while True:
            print("Raqam faqat UZB formatida bo'lishi kerak")
            number = str(input("Raqamni kiriting: "))
            if self.checkNumberFormat(number):
                if self.checkNumberIsHave(number):
                    print("Bu raqam allaqachon mavjud")
                else:
                    price = int(input("Narxini kiriting: "))
                    if price < 0:
                        print("Narx 0 dan katta bo'lishi kerak")
                        continue
                    newNumber = Number(id=len(numbers_list) + 1, number=number, price=price)
                    numbers_list.append(newNumber)
                    print("Raqam qo'shildi")
                    break
            else:
                print("Raqam xato formatda !")

    def delNumber(self):
        self.numberList()
        delId = input("Raqam id ni kiriting: ")
        if delId.isdigit():
            if self.checkIdIsHave(int(delId)):
                sure = input("Raqamni o'chirmoqchimisiz ? (ha/yo'q): ")
                if sure == "ha":
                    carNumber = self.getNumberById(int(delId))
                    numbers_list.remove(carNumber)
                    print("Raqam o'chirildi")
                else:
                    print("Raqam o'chirish bekor qilindi")
            else:
                print("Raqam mavjud emas")
        else:
            print("Raqam id ni xato formatda !")

    def delNumberByNumber(self, number: Number):
        sure = input("Raqamni o'chirmoqchimisiz ? (ha/yo'q): ")
        if sure == "ha":
            carNumber = number
            numbers_list.remove(carNumber)
            print("Raqam o'chirildi")
        else:
            print("Raqam o'chirish bekor qilindi")

    def editNumberByNumber(self, number: Number):
        while True:
            carNumber = number
            carNumberEdit = input(f"Raqamni o'zgartiring(xozirgi - {carNumber.number}): ")
            if self.checkNumberFormat(carNumberEdit):
                if self.checkNumberIsHave(carNumberEdit):
                    print("Bu raqam allaqachon mavjud")
                else:
                    priceEdit = input("Narxni o'zgartiring(xozirgi - {carNumber.price}): ")
                    if priceEdit.isdigit():
                        if int(priceEdit) < 0:
                            print("Narx 0 dan katta bo'lishi kerak")
                            continue
                        carNumber.price = priceEdit
                        carNumber.number = carNumberEdit
                        print("Raqam malumotlari o'zgartirildi")
                        break
                    else:
                        print("Narx xato formatda !")
            else:
                print("Raqam xato formatda !")

    def editNumber(self):
        self.numberList()
        editId = input("Raqam id ni kiriting: ")
        if editId.isdigit():
            if self.checkIdIsHave(int(editId)):
                sure = input("Raqamni o'zgartirmoqchimisiz ? (ha/yo'q): ")
                if sure == "ha":
                    while True:
                        carNumber = self.getNumberById(int(editId))
                        carNumberEdit = input(f"Raqamni o'zgartiring(xozirgi - {carNumber.number}): ")
                        if self.checkNumberFormat(carNumberEdit):
                            if self.checkNumberIsHave(carNumberEdit):
                                print("Bu raqam allaqachon mavjud")
                            else:
                                priceEdit = input("Narxni o'zgartiring(xozirgi - {carNumber.price}): ")
                                if priceEdit.isdigit():
                                    if int(priceEdit) < 0:
                                        print("Narx 0 dan katta bo'lishi kerak")
                                        continue
                                    carNumber.price = priceEdit
                                    carNumber.number = carNumberEdit
                                    print("Raqam malumotlari o'zgartirildi")
                                    break
                                else:
                                    print("Narx xato formatda !")
                        else:
                            print("Raqam xato formatda !")

                else:
                    print("Raqam o'zgartirish bekor qilindi")
            else:
                print("Raqam mavjud emas")
        else:
            print("Raqam id ni xato formatda !")

    def soldNumberList(self):
        if len(numbers_list) != 0:
            filteredSoldNumbers = [number for number in numbers_list if number.isSold]
            if len(filteredSoldNumbers) != 0:
                for number in filteredSoldNumbers:
                    print(
                        f"Raqam: {number.number} | Narx: {number.price} | Raqam egasi : {user_list[number.owner].username}")
            else:
                print("Sotilgan raqamlar ro'yxati bo'sh")
        else:
            print("Sotilgan raqamlar ro'yxati bo'sh")

    def findNumber(self, query) -> list[Number]:
        newList = []
        for number in numbers_list:
            if query in number.number:
                newList.append(number)
        return newList

    def searchNumber(self):
        if len(numbers_list) != 0:
            number = str(input("Raqamni kiriting: "))
            foundList = self.findNumber(number)
            if len(foundList) != 0:
                while True:
                    for number in foundList:
                        print(
                            f"Raqam: {number.number} | Narx: {number.price} | Raqam egasi : {user_list[number.owner].username}")
                    print("1-> Raqamni o`chirish")
                    print("2-> Raqamni o`zgartirish")
                    print("3-> Chiqish")
                    choice = input("Tanlash: ")
                    if choice == "1":
                        carNumId = input("Raqam id ni kiriting: ")
                        if carNumId.isdigit():
                            if self.checkIdIsHave(int(carNumId)):
                                self.delNumberByNumber(self.getNumberById(int(carNumId)))
                            else:
                                print("Raqam mavjud emas")
                        else:
                            print("Raqam id ni xato formatda !")

                    elif choice == "2":
                        carNumId = input("Raqam id ni kiriting: ")
                        if carNumId.isdigit():
                            if self.checkIdIsHave(int(carNumId)):
                                self.editNumberByNumber(self.getNumberById(int(carNumId)))
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

    def mostSoldUser(self):
        if len(numbers_list) != 0:
            filteredSoldNumbers = [number for number in numbers_list if number.isSold]
            if len(filteredSoldNumbers) != 0:
                mostSoldUser = max(filteredSoldNumbers, key=lambda x: x.owner)
                print(f"Eng ko'p raqam sotib olgan foydalanuvchi: {user_list[mostSoldUser.owner].username} | Raqamlar soni: {len(filteredSoldNumbers)}")
            else:
                print("Sotilgan raqamlar ro'yxati bo'sh")
        else:
            print("Sotilgan raqamlar ro'yxati bo'sh")

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
                return
            else:
                print("Tanlashda xatolik !\n")
