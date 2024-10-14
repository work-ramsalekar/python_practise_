from ast import Not


class Contact:

    def __init__(self,name = None , phno = None,):
        self.name = name
        self.phno=phno
        

    def __str__(self) -> str:
        return f"Name : {self.name} Phone No : {self.phno}"
    
    def updateContact(self,newContact):
        self.name = newContact.name
        self.phno = newContact.phno


contactList = []

start = True
   
while(start) :
        print()
        print("0 : to exit")
        print("1 : add New Contact")
        print("2 : View all Contact")
        print("3 : update existing contact by name ")
        print("4 : Delete by Name")
        print("5 : Search by name ")
        print()

        choose = int(input("Enter the choose "))
        if(choose == 0):
            start = False
            break;
        elif (choose == 1):
            cname = input("Enter the contact name ")
            cphn = int(input("Enter the contact phno:"))
            contactList.append(Contact(cname,cphn))
            
        elif (choose == 2):
            for contacts in contactList :
                print(contacts)
             
            print()
        
        elif(choose == 3):
             cname = input("Enter the contact name ")
             cphn = int(input("Enter the contact phno:"))
             flag = False
             for contacts in contactList:
                 if(cname == contacts.name):
                     contacts.phno = cphn
                     print("Update sucessfully")
                     flag = True
                     break;
             
             if not flag :
                 contactList.append(Contact(cname,cphn))
        
        elif(choose ==4 ):
            cname = input("Enter the name : ")
            for i in contactList:
                flag = True
                if(i.name == cname):
                    contactList.remove(i)
                    print("Delte sucessfull")
                    flag = False
                    break
                if not flag :
                    print("Not found ")

        elif (choose == 5 ):
            cname = input("Enter the name  : ")
            for i in contactList :
                flag = True
                if(i.name == cname):
                    print(i)
                    flag = False
                    break
                if(flag):
                    print("No such contact")

        else:
            print("You choose Wrong option")




             
            
            

