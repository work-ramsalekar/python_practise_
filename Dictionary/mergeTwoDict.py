def merge(dict1 : dict , dict2 : dict) -> dict :
    ans = {}
    for i in dict1 :
        if i in dict2 :
        
            ans[i] = dict1[i] + dict2[i]
        else :
            ans[i] = dict1[i]
    for i in dict2 :
        if not i in dict1 :
            ans[i] = dict2[i]
    return ans



dict1 = {
    "a" : 1,
    "b" : 1,
    "c" : 1,
    "e" : 3
}

dict2 = {
    "a" : 2,
    "b" : 5,
    "c" : 4,
    "d" : 6
}



print(dict1 , " and ", dict2)

print("After Merging ")

print(merge(dict1,dict2))

