add = lambda x ,y,z : x+y+z

# lambda name = (keyword) lambda space between parameter and keyword   all parameters seprated by , and then after : the result

print(add(4,4,4))
print("********************************")

maximum = lambda x,y,z : max(x,y,z)

print(maximum(100,200,300))

print("********************************")

def square(num ) :
    return num ** 2

mylist = [1,2,3,4,5,6]

k = map(square,mylist)

print(list(k))

print("**************************************")

divide = lambda  x,y : x/y

print("This is map functional programming : ")
print(list(map(divide,[4,6,8],[2,3,4])))
print("**************************************")
even = lambda x : x % 2 == 0 
mylist = list(filter(even , mylist))
print(mylist)
print("*****************************************")
def prime (num) :
    for i in range (2 , num) :
        if(num % i == 0 ):
         return False
    return True

primelist = [i for i in range (2,100)]

print(list(filter(prime,primelist)))
