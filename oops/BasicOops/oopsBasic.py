class Cdac :
    def __init__(self , name = None, marks = None):
        self.name = name
        self.marks = marks

    def total(self) -> float:
        sum = 0
        for i in self.marks:
            sum+=i
        return sum
    
    def avg (self) -> float:
        sum = 0;
        for i in self.marks :
            sum+=i
        return sum / len(self.marks)






c = Cdac("ram",[93,100])
print(c.marks)

print(c.total())

print(c.avg())