from accType import AccountType
from Bank import Account
from BankException import AccounException


class CRUD:
    @staticmethod
    def CreateAccount(accountNum,name,pin,type,balance) ->Account :
        try :
            act = AccountType(type)
            return Account(accountNum,name,pin,act,balance)

        except :
            raise AccounException("This type of account is not possiable :-< ")
         
