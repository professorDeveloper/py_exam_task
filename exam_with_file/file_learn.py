import json

from exam.number import Number


#
# json_data = {
#     "username": "admin",
#     "password": "1234",
#     "address": "Toshkent"
#     , "number": [
#         {
#             "id": 1,
#             "number": 12345678,
#             "price": 10000,
#             "isSold": True,
#             "owner": "admin"
#         }
#     ]
# }
# file_path = "user.json"
# with open(file=file_path, mode="w") as file:
#     json.dump(json_data, file,indent=4)
#     print(f"json data: {file_path} was created")
#
# with open(file=file_path, mode="r") as file:
#     data = json.load(file)
#
#     print(f"json data: {data}")

def writeList(list: list, file_path: str):
    with open(file=file_path, mode="w") as file:
        json.dump(list, file,indent=4)


def readList (file_path: str) -> list:
    with open(file_path, "r") as file:
        data = json.load(file)
        numbers_list =[]
        for number in data:
            numbers_list.append(Number.from_dict(number))
        return numbers_list

writeList([Number(id=1, number="12345678", price=10000, isSold=True,).to_dict()], "list.json")

read_numbers = readList("list.json")
for number in read_numbers:
    print(f"ID: {number.id}, Number: {number.number}, Price: {number.price}, Is Sold: {number.isSold}")
