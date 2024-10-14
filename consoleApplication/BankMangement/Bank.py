from accType import AccountType

class Account :
    def __init__(self,accountNum,name,pin,type:AccountType,balance):
        self.accountNum = accountNum
        self.name = name
        self.pin = pin
        self.type = type
        self.balance = balance

    def __str__(self) -> str:
        return f"{self.accountNum} : {self.name}  : {self.balance}"
    
    