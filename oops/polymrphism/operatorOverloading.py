class Student :
    def __init__(self,phy,maths):
        self.phy = phy
        self.maths = maths
    
    def __add__(self,other):
        return(self.phy+other.phy , self.maths + other.maths)
    


class main :
    std1 = Student(100,100)
    std2 = Student(50,50)

    print(std1+std2)