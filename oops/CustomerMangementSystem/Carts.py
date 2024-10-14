class cart :
    def __init__(self,lists,totalprice):
        self.lists = lists
        self.price = totalprice
    
    def __str__(self) -> str :
        return f" the list is : {self.lists}   and total price is : {self.price}"
