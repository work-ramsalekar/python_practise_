from Customer import Customer
from Plan import Plan
from Items import Item
from itemUtilty import Utility
from CustomerException import CustomerException
from applicationUtility import *

class Main :
    try :
        print("Welcom to Customer Mangement Application ")
        itemdb = Utility.populateitemList()
        customerdb = Utility.populateCustomerList()
        
        cId = 5
        iId = 5
        end = False
        

        while not end :
          try :  
                print(
                '''
                0 : exit
                1 : add new Customer
                2 : view all customer
                3 : login specific customer
                4 : admin login

                ''' )
                ch= int(input("enter choice : "))
                
                if (ch == 0) :
                    print("Thanks visit again :-) ")
                    end = True
                    break
                
                elif (ch ==1 ):
                     cname = input("Enter Name : ")
                     pswd = input("enter password : ")
                     p = input("Select plan : gold , silver , diamond : ")
                    
                     customerdb.append(ApplicationUtility.vaildateCustomer(cId,cname,pswd,p))
                     cId+=1
                
                elif(ch == 2) : 
                     sortcust = list(sorted(customerdb , key = lambda x : x.plan))
                     for i in sortcust :
                          print(i)

                elif (ch == 3) :
                     cname = input("enter user name : ")
                     pwd = input("Enter password : ")
                     cst = ApplicationUtility.login(cname,pwd,customerdb)
                     print(cst.cName , " Login sucessfully ")

                     flag = False
                     while not flag :
                          print(
                               '''
                                1 : Logout
                                2 : add items in cart
                                3 : view total bill and cart items
                                4 : remove item from cart
                            '''
                          )
                          c = int(input("Enter choice : "))
                          if (c == 1) :
                               flag = True
                               break
                          
                          elif(c == 2) :
                                Utility.showitems(itemdb)
                                ic = int(input("enter item id for add into cart : "))
                                item = Utility.addItem(itemdb,ic)
                                cst.addToCart(item)

                          elif (c == 3) :
                               print("Cart Items : ",cst.showCart())
                               print()

                               print("Total bill is : ",cst.totalBill())
                            
                          elif(c == 4) :
                                 id = int(input("Enter id of product for remove : "))
                                 cst.removeItem(id)
                
                elif (ch == 4) :
                     userName = input("Enter UserName : ")
                     pwd = input("Enter Password : ")
                     flag= False
                     while not flag :
                          if(userName == "admin" and pwd == "admin"):
                           print(
                               '''
                              0 : logout 
                              1 : add new item in shop
                              2 : remove item from shop
                              3 : print all customer Details : 
                               
                               '''
                          )
                          ch = int(input("select Options : "))

                          if(ch == 1):
                               iname = input("Enter item name : ")
                               iprice = int(input("Enter price"))
                               itemdb.append(Item(iId,iname,iprice))
                               iId +=1
                               print("add Sucessfully")
                          
                          elif(ch == 2) : 
                               for i in itemdb :
                                    print(i)
                               cid =int(input("Enter id to delete item from shop  "))
                               itemdb = ApplicationUtility.deletebyid(itemdb,cid)
                               print("Remove sucessFully")

                          elif (ch == 3):
                               ApplicationUtility.writeintext(customerdb)
                            
                          elif(ch == 0) :
                               flag = True
                               break
                               


                          
                           



                                    
                    

                

          except CustomerException as c :
                    print(c)
                 
                  
    except Exception as e :
        print(e)