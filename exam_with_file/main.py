from file_utils import  writeList,readList,readListUser,deleteById,deleteByIdUser,updateById,updateByIdUser,updateUserNumbers,changeNumberOwner
from share_data import user_file,numbers_file
from models import User,Number

user = User(
    username="user1",
    password="1234",
    address="Tashkent"
)

user.numbers = [Number(id=1, number="1234", owner=user), Number(id=2, number="2345", owner=user)]

user_list =[user]

writeList(user_list, user_file)
print(readListUser(user_file)[0].username)