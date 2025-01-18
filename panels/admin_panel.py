from utils.file_utils import readListUser, readList, writeList
from models.models import Number, User

user_file = "users.json"
numbers_file = "numbers.json"


class AdminPanel:
    def __init__(self, admin):
        self.__users = readListUser(user_file)
        self.__numbers = readList(numbers_file)
        self.__admin = admin

    ## Admin Panel
    def run(self):
        while True:
            print("1. Foydalanuvchilar ro'yxatini ko'rish")
            print("2. Avto raqamlarini ro`yhati")
            print("3. Avto raqamlarini qo'shish")
            print("4. Avto raqamlarini o'chirish")
            print("5. Avto raqamlarini tahrirlash")
            print("6. Sotilgan raqamlar ro`yhati ")
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

    # Checker methods
    def checkNumberId(self, id: int):
        for number in self.__numbers:
            if number.id == id:
                return True
        return False

    def checkNumber(self, number: str):
        for num in self.__numbers:
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
        for number in self.__numbers:
            if number.id == id:
                return number

    def findNumber(self, query) -> list[Number]:
        newList = []
        for number in self.__numbers:
            if query in number.number:
                newList.append(number)
        return newList

    ## Number methods

    def showNumber(self, number: Number):
        if number.isSold:
            print(
                f"Id: {number.id} | Raqam: {number.number} | Narx: {number.price} | Sotilgan: {number.isSold} | Raqam egasi: {number.owner}")
        else:
            print(f"Id: {number.id} | Raqam: {number.number} | Narx: {number.price} | Sotilgan: {number.isSold}")


    def numberList(self):
        self.__numbers = readList(numbers_file)
        if len(self.__numbers) != 0:
            for number in self.__numbers:
                self.showNumber(number)
        else:
            print("Avto raqamlar ro'yxati bo'sh")

    def requestAddNumber(self):
        number = str(input("Raqamni kiriting: "))
        if self.checkNumber(number):
            print("Bu raqam allaqachon mavjud")
        else:
            price = input("Narxini kiriting: ")
            if price.isdigit():
                price = int(price)
                if price < 0:
                    print("Narx 0 dan katta bo'lishi kerak")
                    return
                newNumber = Number(id=len(self.__numbers) + 1, number=number, price=price)
                self.__numbers.append(newNumber)
                writeList(self.__numbers, numbers_file)
                print("Raqam qo'shildi")
            else:
                print("Narx raqam bo`lishi kerak")

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
                        self.__numbers.remove(carNumber)
                        writeList(self.__numbers, numbers_file)
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
                                writeList(self.__numbers, numbers_file)
                                print("Raqam tahrildi")
                        else:
                            print("Narx xato formatda !")
            else:
                print("Raqam mavjud emas")
        else:
            print("Raqam id ni xato formatda !")

    def soldNumberList(self):
        self.__numbers = readList(numbers_file)
        if len(self.__numbers) != 0:
            filteredSoldNumbers = []
            for number in self.__numbers:
                if number.isSold:
                    filteredSoldNumbers.append(number)
            if len(filteredSoldNumbers) != 0:
                for number in filteredSoldNumbers:
                    print(f"Raqam: {number.number} | Narx: {number.price} | Raqam egasi: {number.owner}")
            else:
                print("Sotilgan raqamlar ro'yxati bo'sh")
        else:
            print(" raqamlar ro'yxati bo'sh")

    def searchNumber(self):
        if len(self.__numbers) != 0:
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
        self.__users = readListUser(user_file)
        if len(self.__users) != 0:
            for user in self.__users:
                print(f"Username: {user.username} | Password: {user.password} | Address: {user.address}")
        else:
            print("Foydalanuvchilar ro'yxati bo'sh")

    def getCountOfNumber(self, owner):
        count = 0
        for number in self.__numbers:
            if number.owner == owner:
                count += 1
        return count

    def mostSoldUser(self):
        if len(self.__numbers) != 0:
            filteredSoldNumbers = [number for number in self.__numbers if number.isSold]
            if len(filteredSoldNumbers) != 0:
                mostSoldUser = min(filteredSoldNumbers, key=lambda x: x.owner)
                print("=============================================================== ")
                print(
                    f"Eng ko'p raqam sotib olgan foydalanuvchi: {mostSoldUser.owner} | Raqamlar soni: {self.getCountOfNumber(mostSoldUser.owner)}")
                print("=============================================================== ")
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
        if int(password) == self.__admin.pinCode:
            self.run()
        else:
            print("Login yoki parol xato !")


