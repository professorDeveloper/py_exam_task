from exam.user import User
class Number:
    def __init__(self, id:int,number:str,isSold:bool=False,price:int=0,owner:User=None):
        self.id=id
        self.number=number
        self.isSold=isSold
        self.price=price
        self.owner=owner
