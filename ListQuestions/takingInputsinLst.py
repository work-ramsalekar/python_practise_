listItems = input("Enter the integer : ")

mylist = listItems.split()

mylist =[ int(items) for items in mylist]

print(mylist)


sum = 0

for i in mylist :
    sum+=i

print("the sum is : ",sum)