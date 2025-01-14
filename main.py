from services.user_service import UserService
from services.admin_service import AdminService

userService = UserService()
adminService = AdminService()

while True:
    print("===================================================")
    print("1. Foydalanuvchi paneli")
    print("2. Admin paneli")
    print("===================================================")
    choice = input("Tanlang: ")
    if choice == "1":
        print("===================================================")
        print("Foydalanuvchi paneliga xush kelibsiz")
        print("1. Ro`yhatdan o`tish")
        print("2. Kirish")
        print("===================================================")
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






def prepare_ingredients():
    print("Sabzavotlarni yuvish, go'shtni kesish.")


def cook():
    print("Pishirish jarayoni: Sabzavotlarni qovurish, go'shtni pishirish.")


def garnish():
    print("Taomni bezash: Yashil giyohlar bilan bezatish.")


def make_dish():
    print("Taom tayyorlashni boshlaymiz:")
    prepare_ingredients()
    cook()
    garnish()
    print("Taom tayyor!")


make_dish()
