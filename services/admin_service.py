from share_data.share_data import user_file, numbers_file
from utils.file_utils import readListUser, readList, writeList
from models.models import Number, User


class AdminService:
    def __init__(self, admin):
        self.users = readListUser(user_file)
        self.numbers = readList(numbers_file)
        self.admin = admin

    # Checker methods
    def checkNumberId(self, id: int):
        for number in self.numbers:
            if number.id == id:
                return True
        return False

    def checkNumber(self, number: str):
        for num in self.numbers:
            if num.number == number:
                return True
        return False

    def checkNumberFormat(self, number: str):  ## 50 R174QA
        if len(number) == 8:
            if (number[0].isdigit() and number[1].isdigit() and number[2].isalpha() and number[3].isdigit() and
                    number[4].isdigit() and number[5].isdigit() and number[6].isalpha() and number[7].isalpha()):
                return True
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
    def showNumber(self, number: Number):
        if number.isSold:
            print(f"Id: {number.id} | Raqam: {number.number} | Narx: {number.price} | Sotilgan: {number.isSold} | Raqam egasi: {number.owner.username}")
        else:
            print(f"Id: {number.id} | Raqam: {number.number} | Narx: {number.price} | Sotilgan: {number.isSold}")

    def numberList(self):
        self.numbers = readList(numbers_file)
        if len(self.numbers) != 0:
            for number in self.numbers:
                self.showNumber(number)
        else:
            print("Avto raqamlar ro'yxati bo'sh")

    def requestAddNumber(self):
        while True:
            print("Raqam faqat UZB formatida bo'lishi kerak (50R174QA)")
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

    def soldNumberList(self):
        if len(self.numbers) != 0:
            filteredSoldNumbers = [number for number in self.numbers if number.isSold]
            if len(filteredSoldNumbers) != 0:
                for number in filteredSoldNumbers:
                    print(f"Raqam: {number.number} | Narx: {number.price} | Raqam egasi: {number.owner.username}")
            else:
                print("Sotilgan raqamlar ro'yxati bo'sh")
        else:
            print("Sotilgan raqamlar ro'yxati bo'sh")

    def searchNumber(self):
        if len(self.numbers) != 0:
            number = str(input("Raqamni kiriting: "))
            foundList = self.findNumber(number)
            if len(foundList) != 0:
                for number in foundList:
                    self.showNumber(number)
            else:
                print("Raqam mavjud emas")
        else:
            print("Raqamlar ro'yxati bo'sh")

    ## User methods
    def userList(self):
        self.users = readListUser(user_file)
        if len(self.users) != 0:
            for user in self.users:
                print(f"Username: {user.username} | Password: {user.password} | Address: {user.address}")
                if len(user.my_numbers) != 0:
                    print(f"  Sotib olingan raqamlar:")
                    for number in user.my_numbers:
                        print(f"    Id: {number.id} | Raqam: {number.number} | Narx: {number.price} | Sotilgan: {number.isSold}")
                else:
                    print("  Foydalanuvchi hech qanday raqam sotib olmagan.")
        else:
            print("Foydalanuvchilar ro'yxati bo'sh")

    def mostSoldUser(self):
        if len(self.numbers) != 0:
            filteredSoldNumbers = [number for number in self.numbers if number.isSold]
            if len(filteredSoldNumbers) != 0:
                mostSoldUser = max(filteredSoldNumbers, key=lambda x: x.owner)
                print(f"Eng ko'p raqam sotib olgan foydalanuvchi: {mostSoldUser.owner.username} | Raqamlar soni: {len(filteredSoldNumbers)}")
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
        if int(password) == self.admin.pinCode:
            self.adminPanel()
        else:
            print("Login yoki parol xato !")

    ## Admin Panel
    def adminPanel(self):
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
