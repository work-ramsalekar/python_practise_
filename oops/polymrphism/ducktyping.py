class Bird :
    def fly(self):
        print("Bird can fly")

class Aeroplane :
    def fly(self):
        print("Aeroplane can fly")

def flyableunits(obj):
    obj.fly()



flyableunits(Bird())
flyableunits(Aeroplane())