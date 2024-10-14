def bs(mylist : list , key) -> int :
    start = 0
    end = len(mylist) - 1

    while (start <= end) :
        mid = (start + end) // 2
        if(mylist[mid] == key) :
            return mid
        elif(mylist[mid] > key) :
            end = mid -1
        else :
            start = mid + 1
    return -1



mylist = [1,2,3,4,5,6,7,8]
i = int(input("enter id : "))
print(bs(mylist , i))