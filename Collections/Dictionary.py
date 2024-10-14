from collections import OrderedDict
from collections import defaultdict
from collections import Counter

nd = dict()
od = OrderedDict()

nd["c"] = 3
nd["a"] = 1
nd["b"] = 2

od["c"] = 3
od["a"] = 1
od["b"] = 2


for key,value in nd.items() :
    print(key,value)
print("******************************")
for key,value in od.items() :
    print(key,value)

od.move_to_end("c")
print("******************************")
for key,value in od.items() :
    print(key,value)


od.move_to_end("b",False)

print("******************************")
for key,value in od.items() :
    print(key,value)

print("***************************************************************************************************")

counts = Counter([1,4,1,4,2,4,2,1,3,3,3,7,0])

print(counts)

stringcounter = Counter("helloshldsljweljw")
print(stringcounter)
print("*********")
print(stringcounter.most_common(3))

stringcounter.subtract("h")
print("**********",stringcounter)

stringcounter.update({"l": 10})
print("**********",stringcounter)

print("*********************************************************************************************************************88")

print()
print()
print("Default dictionary : ")

items = [('fruit', 'apple'), ('fruit', 'banana'), ('vegetable', 'carrot')]
grouped = defaultdict(list)

for val , item in items :
    grouped[val].append(item)

print(grouped)