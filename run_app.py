from panels.user_panel import UserPanel
from panels.admin_panel import AdminPanel
from models.models import Admin

admin = Admin(pinCode=1234)
userPanel = UserPanel()
adminPanel = AdminPanel(admin=admin)

def runApp():
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
                userPanel.userRegister()
            elif choice == "1":
                userPanel.userLogin()
            else:
                print("Xato tanlov")
        elif choice == "2":
            adminPanel.loginAdmin()
        else:
            print("Xato tanlov")
