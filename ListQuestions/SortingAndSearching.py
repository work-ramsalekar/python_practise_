 


def sorting(my_list : list[int]):
    size = int(len(my_list))

    for i in range (0, size -1):
        for j in range (i+1 , size):
            if(my_list[i] > my_list[j]):
                temp = my_list[i]
                my_list[i] = my_list[j]
                my_list[j]=temp




my_list = [102,55,44,100,33,97,22,2,11]

print("Before sort : ",my_list)

sorting(my_list)



print("After Srting : " ,my_list)

my_list.sort(reverse=True)
print(my_list)