from exam.user import User
from exam.number import Number
from exam.admin import Admin

user_data ="user_data.json"
admin_data = "admin_data.json"
numbers_data = "numbers_data.json"
user_list: list[User] = []
numbers_list: list[Number] = []
admin = Admin(pinCode="1234")
