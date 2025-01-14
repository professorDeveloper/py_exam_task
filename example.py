from models.models import Number

number =Number.from_dict({"id": 1, "number": "50R174QA", "price": 50000, "isSold": False, "owner": None})
print(number.price)