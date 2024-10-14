def fib(a,b,counts) :
    if(counts - 1 == 0) :
        return

    print(a+b , end = " ")
    counts-=1
    c = a+b
    fib(b,c,counts)



fib(0,1,int(input("Enter how many you want : ")))