def bs(start,end,key,arr) :
    if(start > end) :
        return -1
    mid = (start + end) // 2
    if(arr[mid] == key):
        return mid
    
    elif(arr[mid] > key):
        end = mid -1
        return  bs(start,end,key,arr)

    else :
        start = mid +1
        return  bs(start,end,key,arr)



arr = [11,22,33,44,55]

print(bs(0,len(arr)-1,2,arr))