from exam.admin_service import AdminService
from exam.user_service import UserService
from exam.share_data import admin

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
        pass
    elif choice == "3":
        break
    else:
        print("Tanlashda xatolik !\n")