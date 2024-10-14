'''
listItems = input("Enter items separated by space ")

mylist = listItems.split()

mylist = [int(item) for item in mylist]


print("the list is : ",mylist)

sum = 0
for item in mylist :
    sum+=item

print("The sum is : ",sum)
    '''

#taking inputs from user
listitems = input("Enter the integer : ")

#add all items in the list
mylist=listitems.split()

#convert the items into integer
mylist = [int(items)  for items in mylist]

#printing whole list
print(mylist)

#printing each item of the list

for it in mylist:
  print(it,end = " ")

