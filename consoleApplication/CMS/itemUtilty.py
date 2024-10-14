from Items import Item
from Customer import Customer
from Plan import Plan
from CustomerException import *

class Utility :
    @staticmethod
    def populateitemList() -> list :
        popList = []
        popList.append(Item(1,"Soap",20))
        popList.append(Item(2,"Biscuit",30))
        popList.append(Item(3,"Chips",40))
        popList.append(Item(4,"Pen",100))

        return popList
        
    @staticmethod
    def populateCustomerList() -> list :
        poplist = []
        poplist.append(Customer(101,"Ram",Plan.DIAMOND,"123"))
        poplist.append(Customer(102,"Sid",Plan.SILVER,"456"))
        poplist.append(Customer(103,"Guru",Plan.GOLD,"789"))
        poplist.append(Customer(104,"atul",Plan.SILVER,"333"))
        return poplist

    @staticmethod
    def showitems(itemdb : list):
        for i in itemdb :
            print(i)
        
    @staticmethod
    def addItem(itemdb : list , choice) -> Item :
       i = next((it for it in itemdb if(it.iId == choice)),None)

       if i is None :
        raise CustomerException("You choose wrong id from above list")
       return i
       