class Student:

    def __init__(self,name = None,maths=None,science=None,history=None):
        self.name = name
        self.maths = maths
        self.science = science
        self.history = history

    def theAvg(self) -> float :
        return (self.maths+self.history+self.science)/3



