from Customer import *
from Plan import *
from Items import *
from CustomerException import *

class ApplicationUtility :
    @staticmethod
    def vaildateCustomer(id,cname,pswd,plan) -> Customer :
        p = ApplicationUtility.validatePlan(plan)
        return Customer(id,cname,p,pswd)


    @staticmethod
    def validatePlan(pl) -> Plan :
        try :
            return getattr(Plan,pl.upper())
           
        except KeyError  :
            raise CustomerException("Wrong plan select")
        
    @staticmethod
    def login(username,pwd,db : list) -> Customer :
        cst = next((c for c in db if c.cName == username and c.pswd == pwd),None)
        
        if cst is None :
            raise CustomerException("Invalid Login")
        
        return cst
        
    @staticmethod
    def writeintext(li : list) :
        with open("mycustlist.txt","w+") as fi :
            for i in li :
                fi.write(str(i) + "\n")
        print("Write Sucessfully")
    @staticmethod
    def deletebyid(itemdb : list , cid)-> list :
        itemdb = list(filter(lambda x: x.iId != cid , itemdb))
        return itemdb