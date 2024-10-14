def toDic(word : str) -> dict:
    ans = {}
    for char in word :
        if char in ans :
            ans[char] +=1
        else :
            ans[char] = 1
    return ans


def listToDic(mylist : list) -> dict :
    ans ={}
    for i in mylist :
        if i in ans :
            ans[i] +=1
        else :
            ans[i] = 1
    return ans







inte = input("Enter all numbers in list  ")

mylist = inte.split()

mylist = [int(items) for items in mylist]
print(listToDic(mylist))
