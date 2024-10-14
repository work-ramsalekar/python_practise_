mydict = {
    "h" : 1,
    "e" : 1,
    "l" : 2,
    "o" : 1
}

print("Before adding new element : ",mydict)

key = input("Enter key ")
value = int(input("Enter value "))
mydict[key] = value

print(mydict)