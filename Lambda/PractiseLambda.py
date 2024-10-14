def prime(num) -> bool:
    if(num == 2) :
        return True
    
    for i in range (2,num):
        if(num % i == 0):
            return False
        
    return True


mylist =[x for x in range (2,101)]

print(mylist)

primelist = list(filter(prime,mylist))

print(primelist)

print("Above is filter****************************************")

def extractFirstLetter(word) -> str :
    return word[0]

words = ["apple", "banana", "cherry", "date"]

ans = list(map(extractFirstLetter,words))

print(ans)

print("*************************************************")

stringlist = ["1","2","3","4"]

def con (wo) -> int :
    return int(wo)

ilist = list(map(con,stringlist))

ilist2 = list(int(x) for x in stringlist )


print(ilist)
print(ilist2)

print("*********************************")

def connect (wo , wo2) ->str :
    return wo +" "+ wo2 



first_names = ["John", "Jane", "Doe"]
last_names = ["Doe", "Smith", "Johnson"]

fullname = list(map(connect,first_names,last_names))

print(fullname)



"*******************Map + filter : ********************************"
numlist = [int(x) for x in range (1 , 21)]

print(numlist)

def isEven(num ) -> bool :
    if(num % 2 == 0) :
        return True
    return False

def square(num) -> int :
    return num **2


mapfillist = list(map(square,list(filter(isEven,numlist))))

print(mapfillist)

"***************************************************"

fruits = ["apple", "banana", "cherry"]

print(list(map((lambda x : len(x)) , fruits)))

print("*************************************************")

print(list(map((lambda x : x*2),[x for x in range (1 , 20 ,2)])))