class Bank :
    def __init__(self,name = None,accno = None,balance = None,pin = None):
        self.name = name
        self.accno = accno
        self.balance = balance
        self.pin = pin

    def getinfo(self):
        print("Name : ",self.name , " Balance is : ",self.balance)

    def deposit(self , amount):
        self.balance+=amount

    def withdraw(self,amount,pin) -> bool:
        if(self.balance >= amount and self.pin == pin):
            self.balance-=amount
            print("Withdraw Sucessfully")
            return True;
        else:
             print("Withdraw Failed")
             return False;
    
    def transfer(self,act1,amt,pin):
        if(self.withdraw(amt,pin)):
            act1.deposit(amt)
        else:
            print("Transaction failed ")

    def __str__(self) -> str:
         return f"Name : {self.name} AccountNo : {self.accno} Balance : {self.balance}"
    



act1 = Bank("Ram",1234,5000,2140)
act2 = Bank("Sid",2345,2000,0000)

print("Before transaction : ")
act1.getinfo()
act2.getinfo()
print("**************************")

act1.transfer(act2,200,2140)
print("After transaction : ")
act1.getinfo()
act2.getinfo()
print("**************************")

mydb = [act1,act2]

for acts in mydb:
     print(acts)




 




