mylist = ["Cherry","Apple" , "apple","mango" , "cherry"]

ans=  next((mylist.index(items) for items in mylist if items == "mango"),None)


print(ans)
