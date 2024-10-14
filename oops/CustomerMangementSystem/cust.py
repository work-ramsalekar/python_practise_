
class Customer:
    def __init__(self,id, name,password,cart):
        self.name = name
        self.password = password
        self.id = id
        self.cart = cart

    def __str__(self) -> str:
        return f"id : {self.id}  Name : {self.name}  the cart details below : {self.cart} "

