
try :
    mylist=[1,2]
    print(mylist[0])
    print(mylist[1])
    print(mylist[100])


except IndexError :
    print("this is ou of bound error")
