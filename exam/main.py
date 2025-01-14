from exam.admin_service import AdminService
from exam.user_service import UserService
from exam.share_data import admin
from exam.user import User


def main():
    adminService = AdminService()
    userService = UserService()

    while True:

        print("Avtomobil raqamlari do'koniga xush kelibsiz")
        print("1. Admin")
        print("2. Foydalanuvchi")
        print("3. Chiqish")

        choice = input("tanlash: ")
        if choice == "1":
            pinCode = input("PIN kodini kiriting: ")
            if pinCode == admin.pinCode:
                adminService.adminPanel()
            else:
                print("Pin code xato")
        elif choice == "2":
            print("1. Kirish")
            print("2. Ro'yxatdan o'tish")
            choice = input("Tanlash: ")
            if choice == "1":
                userService.userLogin()
            elif choice == "2":
                userService.userRegister()
            else:
                print("Tanlashda xatolik !\n")
        elif choice == "3":
            break
        else:
            print("Tanlashda xatolik !\n")

main()