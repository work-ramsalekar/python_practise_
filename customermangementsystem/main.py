from cart import items
from customer import Customer

def selectcustomer(cl , id)-> Customer :
   for i in cl :
      if(i.id == id):
         return i


class main :
   print("Welcome to customer mangement app : ")

   Customers = []
   
   itemslist =[]
   itemslist.append(items(1,"soap","bathing soap",20))
   itemslist.append(items(2,"biscuit","snacks",10))
   itemslist.append(items(3,"chips","snacks",30))

   Customers.append(Customer(1,"ram",[itemslist[0],itemslist[2] ]))

   Customers.append(Customer(2,"rock",[itemslist[1],itemslist[2] ]))



   end = True
   customerid = 3
   itemid = 4

   while(end):
      print(
         '''
          0 : exit 
          1 : add new customer 
          2 : view all customer
          3 : add items in custmer cart 
          4 : add new items in shop 
          5 : show bill of customer 
          6 : print bill

           '''
      )
      choose = int(input("Enter choice "))
      if(choose == 0):
         end = False
         break
      
      elif(choose == 1):
         cname = input("Enter your name : ")
         cartlist = []
         Customers.append(Customer(customerid,cname,cartlist))
         customerid +=1
        
      elif(choose == 2):
         for cust in Customers :
            print(cust.name , "  items in cart  : " )
            for i in cust.cart :
               print(i.name)
            print("************************************************")   
              
         
      elif(choose == 3):
         for cust in Customers :
            print(cust)
         print("select id of customer")
         id = int(input("Enter id : "))
         buyingcust = selectcustomer(Customers,id)
         
         stop = True
         while(stop):
            print(
               '''
                 0: checkout
                 1 : add next item
                    '''
            )
            cc = int(input("Enter choice : "))
            if(cc == 0):
               stop = False
               break
            elif(cc == 1):
               for i in itemslist :
                  print(i)
            choseoption = int(input("Enter above item id for add to cart "))
            for i in itemslist:
               if(i.id == choseoption):
                  buyingcust.cart.append(i)
                  for c in Customers:
                     if(c.id == buyingcust.id):
                        c = buyingcust
            print("add sucess fully ")

      elif(choose == 4):
         itemnae = input("Enter the new item name")
         itemDesc = input("Enter its descrption ")
         itemprice = int(input("Enter price for this "))
         itemslist.append(items(itemid,itemnae,itemDesc,itemprice))
         itemid+=1

      elif(choose == 5) :
        for c in Customers:
         print(c.id, "  ",c.name)
         ids = int(input("Enter the id of customer whose want cheack out "))
         bill = 0
         for c in Customers :
            if(c.id == ids):
               for x in c.cart:
                  bill+=x.price
        print("The total bill is ",bill)

      elif(choose == 6) :
         with open("bill.txt", "w+") as billFile:
          for customer in Customers:
            billFile.write(str(customer) )
         
         


   
    
  