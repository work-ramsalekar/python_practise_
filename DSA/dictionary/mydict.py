class myDict :
    def __init__(self) :
        self.size = 100
        self.myarr = [None for i in range (self.size)]

    def myHash(self,key) :
        h = 0
        for char in key :
            h+=ord(char)
        return h % self.size
    
    def set(self,key,val) :
        index = self.myHash(key)
        self.myarr[index] = val

    def get(self,key) :

        return self.myarr[self.myHash(key)]
    
