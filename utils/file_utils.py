import json
import os
from models.models import Number, User
## Number List READ / WRITE in json file Functions
def writeList(numbers: list, file_path: str):
    data =[]
    for number in numbers:
        data.append(number.to_dict())
    with open(file_path, "w") as file:
        json.dump(data, file, indent=4)


def readList(file_path: str) -> list:
    if not os.path.exists(file_path):
        return []
    with open(file_path, "r") as file:
        data = json.load(file)
        returnList =[]
        for item in data:
            returnList.append(Number.from_dict(item))
        return returnList


# User List READ / WRITE in json file Functions

def readListUser(file_path: str) -> list[User]:
    if not os.path.exists(file_path):
        return []
    with open(file_path, "r") as file:
        data = json.load(file)
    return [User.from_dict(item) for item in data]


def writeListUser(users: list, file_path: str):
    data = []
    for user in users:
        data.append(user.to_dict())
    with open(file_path, "w") as file:
        json.dump(data, file, indent=4)
