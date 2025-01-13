from exam.user import User
class Number:
    def __init__(self, id:int,number:str,isSold:bool=False,price:int=0,owner:User=None):
        self.id=id
        self.number=number
        self.isSold=isSold
        self.price=price
        self.owner=owner

    def to_dict(self):
        return {
            "id": self.id,
            "number": self.number,
            "price": self.price,
            "isSold": self.isSold
        }

    @staticmethod
    def from_dict(data):
        return Number(id=data['id'], number=data['number'], price=data['price'], isSold=data['isSold'])

