from functools import reduce

my_tuple = (1,2,"hello",("a",7))



si = len(my_tuple)

for i in range (si) :
    print(my_tuple[i])

print("************************************************************")

input_data = [("Alice", 25), ("Bob", 17), ("Charlie", 30), ("Diana", 19), ("Eve", 20)]

mylist = list(filter(lambda x : x[1] >=18 , input_data))

mylist = list(sorted(mylist, key = lambda x : x[0]))

print(mylist)

print("**********************************************************")

input_data = [("Alice", 25), ("Bob", 17), ("Charlie", 30), ("Diana", 25), ("Eve", 20)]

def todict(people) :
    ans = {}
    for value,key in people :
        if key not in ans :
            ans[key] = []
        ans[key].append(value)
    return ans

print(todict(input_data))

print("************************************************************")

  

sums = reduce(lambda x ,y : x + y[1], input_data , 0 )
print(sums)


    
    