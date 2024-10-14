
#List items are ordered, changeable, and allow duplicate values.


#creating the list (predefined)
my_list = ["apple","banana","mango","mango"]

#priting whole list
print("*********************************************************************************")

print("The list is : ",my_list)
print()

#printing each item with foreach
print("*********************************************************************************")
for items in my_list :
    print("the item is : ",items)

#printing item index based;

print("Index based : ")
#len(..object name..) to find its size 
print("*********************************************************************************")
for i in range (0,len(my_list)) :
    print(my_list[i])

#the type of list is object 
print("*********************************************************************************")
print(type(my_list))
print("*********************************************************************************")

#in single list multiple datatype variable can store 

i = 3
print(type(i)," the type of i and the this item add to this list : ",my_list)
#with the append method we can insert new item in the list
my_list.append(i);
my_list.append(True)
print(my_list)

#print specific range of items in the list :  print(listname[startRange : end Range])
print("*********************************************************************************")
print("Specific range printing : ")
print(my_list[2 : 5]);
print("*********************************************************************************")
 
# count the occurance of the specific items  : listname.count("items whose count to known")
 
print("Count of mango : ",my_list.count("mango"))


# adding multiple item in same time listname.extend(another list /  items)

print("*********************************************************************************")
print("adding multiple item in same time listname.extend(another list /  items)")

anotherlist = [2,"cherry",False,"watermelon",45]

my_list.extend(anotherlist);

print(my_list)
print("*********************************************************************************")
#finding the index of specific item 
print(my_list)
print("the first index of the mango is : ",my_list.index("mango"))


