class Item :
    def __init__(self,id,name,price):
        self.iId = id
        self.iName = name
        self.iPrice = price

    def __str__(self):
        return f"{self.iId} :  {self.iName} : {self.iPrice}"