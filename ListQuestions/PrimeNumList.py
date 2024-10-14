primeList=[];

count = 1;

start = int(input("enter the starting number : "))

end = int(input ("enter the ending number : "))

for i in range (start, end+1):
     is_prime = True
     for j in range (2, i) :
        if(i % j == 0) :
            is_prime = False
     if(is_prime and count < 6):
        primeList.append(i)
        count +=1

print(primeList)