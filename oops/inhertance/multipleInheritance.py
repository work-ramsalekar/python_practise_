class AA :
    @staticmethod
    def calls():
        print("this is from A")

    def speak(self):
        print("This is from A")
     
    def aMetd(self):
        print("this is another from a")

class BB :
    @staticmethod
    def calls():
        print("this is from B")

    def speak(self):
        print("This is from B")

class CC(BB,AA):
    pass



class main :
    a = AA()
    b =BB()
    
    print("This is object of a : ")
   # a.calls()
    a.speak()
    print("This is object of b : ")
    #b.calls()
    b.speak()
    print("######################################")
    c =CC()
    
    


    print("this is from c : ")
    #c.calls()
    c.speak()
    c.aMetd()
    

    print(CC.__mro__)