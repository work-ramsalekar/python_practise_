
fruitList = ["mango","apple","apple","banana","mango","apple"]

#remove the all occurance of apple

print("before removing apple : ",fruitList)


fruitList = [items for items in fruitList  if items != "apple" ] 
print(fruitList)

mylist = [1,2,3,14,6,1,1,3,5];

print("******************************************************")

print("the int list before : ", mylist)

for i in mylist :
    if(i == 1):
        mylist.remove(i)


print("the int list after : ", mylist)



