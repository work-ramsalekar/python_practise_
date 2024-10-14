
class Customer :
    def __init__(self,id:int,name:str,cart: list):
        self.id = id
        self.name = name
        self.cart = cart

    def __str__(self) -> str:
        return f"{self.id} : {self.name} and the cart details is : {self.cart} "