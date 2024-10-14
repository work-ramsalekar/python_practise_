def upper(size):
    for i in range (0 , size+1):
        for j in range (0 , i):
            print(" * ",end="")
        print()


def lower(size):
    for i in range (size , 0, -1):
        for j in range ( i ):
            print(" * ",end ="")
        print()



size = int(input("Enter the size of triangle : "))

print("1 : upper right angle ")
print ("2 : lower Right angle ")

choose = int (input(""))

if(choose == 1):
    print("Upper ")
    upper(size)

elif(choose == 2):
    print("Lower")
    lower(size)



