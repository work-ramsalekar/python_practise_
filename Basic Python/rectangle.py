
def solid(size):
    for i in range (0,size):
        for j in range (0 , size):
            print("*" , end =" ")
        print()

def hollow(size):
    for i in range (0, size):
        for j in range (0 , size):
            if(i == 0 or j == 0 or i == size-1 or j == size -1):
                print("*",end="")
            else :
                print(" ",end="")
        print()



size = int(input("Enter the size of Ractangle : "))
choose = int (input("1 : solid Rectangle  2 : hollow Reactangle : ")) 
print()


if(choose == 1) :
    solid(size)
elif(choose == 2) :
    hollow(size)
