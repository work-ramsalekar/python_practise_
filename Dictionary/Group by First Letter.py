

def groupbyFirst(mylist : list , myset : set) -> dict :
    ans = {}
    
    for i in myset :
        ano = []
        for items in mylist :
            
            if(i == items[0]) :
                ano.append(items)
        ans[i] = ano
        
    return ans  


fruitslist = ["apple", "banana", "apricot", "blueberry", "cherry", "date"]

listofFirst = set()

for fruit in fruitslist :
    listofFirst.add(fruit[0])

print(groupbyFirst(fruitslist,listofFirst))