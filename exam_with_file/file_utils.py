import json
import os
from exam_with_file.models import Number, User


def writeList(numbers: list, file_path: str):
    data = [num.to_dict() for num in numbers]
    with open(file_path, "w") as file:
        json.dump(data, file, indent=4)


def readList(file_path: str) -> list:
    if not os.path.exists(file_path):
        return []
    with open(file_path, "r") as file:
        data = json.load(file)
    return [Number.from_dict(item) for item in data]

def deleteById(file_path: str, id: int) -> str:
    numbers = readList(file_path)
    for i in range(len(numbers)):
        if numbers[i].id == id:
            del numbers[i]
            writeList(numbers, file_path)
            return f"Number with ID {id} deleted."
    return f"Number with ID {id} not found."
def updateById(file_path: str, id: int, new_data: dict) -> str:
    numbers = readList(file_path)
    for number in numbers:
        if number.id == id:
            number.number = new_data.get('number', number.number)
            number.price = new_data.get('price', number.price)
            number.isSold = new_data.get('isSold', number.isSold)
            writeList(numbers, file_path)
            return f"Number with ID {id} updated."
    return f"Number with ID {id} not found."




def readListUser(file_path: str) -> list[User]:
    if not os.path.exists(file_path):
        return []
    with open(file_path, "r") as file:
        data = json.load(file)
    return [User.from_dict(item) for item in data]

def deleteByIdUser(file_path: str, id: int) -> str:
    users = readList(file_path)
    for i in range(len(users)):
        if users[i].id == id:
            del users[i]
            writeList(users, file_path)
            return f"User with ID {id} deleted."
    return f"User with ID {id} not found."
def updateByIdUser(file_path: str, username: int, new_data: dict) -> str:
    users = readList(file_path)
    for user in users:
        if user.username == username:
            user.username = new_data.get('user', user.username)
            user.address = new_data.get('address', user.address)
            user.password = new_data.get('password', user.password)
            writeList(user, file_path)
            return f"User with  {id} updated."
    return f"User {id} not found."


def updateUserNumbers(file_path: str, username: str, new_numbers: list) -> str:
    users = readListUser(file_path)
    found = False
    for user in users:
        if user.username == username:
            found = True
            user.__numbers = [Number.from_dict(num) for num in new_numbers]
            writeList(users, file_path)
            return f"Updated numbers for user {username}."
    if not found:
        return f"User {username} not found."


def changeNumberOwner(file_path: str, number_id: int, new_owner_username: str,user_files_path) -> str:
    numbers = readList(file_path)
    users = readListUser(user_files_path)
    new_owner = None
    for user in users:
        if user.username == new_owner_username:
            new_owner = user

    found = False
    for number in numbers:
        if number.id == number_id:
            found = True
            number.owner = new_owner
            writeList(numbers, file_path)
            return f"Changed owner of number ID {number_id} to {new_owner_username}."
    if not found:
        return f"Number ID {number_id} not found."
