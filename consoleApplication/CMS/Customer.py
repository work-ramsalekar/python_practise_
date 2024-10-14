from Plan import Plan
from Items import Item
class Customer :
    def __init__(self,id,name,plan : Plan,pswd):
        self.cId = id
        self.cName = name
        self.plan = plan
        self.cart = []
        self.pswd = pswd

    def __str__(self):
        return f"Name :  {self.cName}  paln : {self.plan} and  cart : {self.showCart()}"
    
    def showCart(self) -> str :
        ans : str = ""
        for items in self.cart :
            ans += str(items) + " ,"

        return ans
    
    def addToCart(self,i : Item):
        self.cart.append((i))
        print("add sucessfully")

    def totalBill(self) -> int :
        bill = 0
        for i in self.cart :
            
            bill += i.iPrice
        return bill
    
    def removeItem(self,id) :
        self.cart = list(filter(lambda x : x.iId != id , self.cart))
        print("Remove Sucessfully")