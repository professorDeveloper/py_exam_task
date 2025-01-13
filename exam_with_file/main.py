from exam_with_file.services.user_service import UserService
from exam_with_file.services.admin_service import AdminService

userService = UserService()
adminService = AdminService()

while True:
    print("1. Foydalanuvchi paneli")
    print("2. Admin paneli")
    choice = input("Tanlang: ")
    if choice == "1":
        print("Foydalanuvchi paneliga xush kelibsiz")
        print("1. Ro`yhatdan o`tish")
        print("2. Kirish")
        choice = input("Tanlash: ")
        if choice == "1":
            userService.userRegister()
        elif choice == "2":
            userService.userLogin()
        else:
            print("Xato tanlov")
    elif choice == "2":
        adminService.loginAdmin()
    else:
        print("Xato tanlov")
