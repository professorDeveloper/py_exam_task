from services.user_service import UserService
from services.admin_service import AdminService

userService = UserService()
adminService = AdminService()

def minRaqam(numbers):
    smallest = numbers[0]
    for number in numbers:
        if number < smallest:
            smallest = number
    return smallest


numbers = [5, 3, 8, 1, 4]
smallest = minRaqam(numbers)
print(f"Eng kichik raqam: {smallest}")





while True:
    print("===================================================")
    print("1. Foydalanuvchi paneli")
    print("2. Admin paneli")
    print("===================================================")
    choice = input("Tanlang: ")
    if choice == "1":
        print("-----------------------------------------------------------------------")
        print("Foydalanuvchi paneliga xush kelibsiz")
        print("1. Kirish")
        print("2. Ro`yhatdan o`tish")
        print("-----------------------------------------------------------------------")
        choice = input("Tanlash: ")
        if choice == "2":
            userService.userRegister()
        elif choice == "1":
            userService.userLogin()
        else:
            print("Xato tanlov")
    elif choice == "2":
        adminService.loginAdmin()
    else:
        print("Xato tanlov")




