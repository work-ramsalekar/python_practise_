from functools import reduce

employees = [
    {"name": "Alice", "age": 28, "salary": 70000},
    {"name": "Bob", "age": 35, "salary": 80000},
    {"name": "Charlie", "age": 32, "salary": 90000},
    {"name": "David", "age": 29, "salary": 60000},
    {"name": "Eve", "age": 40, "salary": 95000}
]

agel30 = list(filter((lambda x : x["age"] < 30),employees))

print(agel30)
print("************************************************************")

print(list(filter((lambda x : x["name"][1] == "o"),   employees   )))

print("*************************************************************")

print(list(map((lambda x : {x["name"]  ,  x["salary"]+ ((x["salary"] * 10) // 100) } ),employees)))

print("******************************************************************")

l = [x for x in range (1 , 11) ]

print(list(reversed([x for x in range (3, 15)])))

something = "".join(list(reversed("hello")))


print("*****************************************")

somlist = list(something)

print(somlist)

print("*********************************************8")

mylist = [x for x in range (1, 101)] 

totalsum = reduce(lambda x , y : x+y, mylist)
product  = reduce(lambda x,y : x * y , mylist)

print(reduce((lambda x,y : x if x > y else y), mylist))

print("Total sum : ",totalsum)

print("procut is : ",product)

print("******************************")

