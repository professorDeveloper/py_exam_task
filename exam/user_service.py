from exam.share_data import  user_list
from exam.user import User
from exam.number import Number
from exam.share_data import numbers_list

class UserService:

    def checkUserIsHave(self, username, password):
        for user in user_list:
            if user.username == username and user.password == password:
                return True
        return False
    def checkUserName(self, username):
        for user in user_list:
            if user.username == username:
                return True
        return True

    def userPanel(self):
        pass
    def userLogin(self):
        login = input("Login: ")
        password = input("Password: ")
        if self.checkUserIsHave(login, password):
            self.userPanel()
        else:
            print("Foydalanuvchi mavjud emas")


    def userRegister(self):
        while True:
            username = input("Username: ")
            if not self.checkUserName(username):
                password = input("Password: ")
                address = input("Address: ")
                user = User(username, password, address)
                user_list.append(user)
                print("Foydalanuvchi qo'shildi")
            else:
                print("Foydalanuvchi username mavjud !")