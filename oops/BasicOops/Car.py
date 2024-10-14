class Engine :
    
    def __init__(self,piston = None,types = None):
        self.piston = False
        self.types = False
    
    
    def toStart(self):
        self.piston = True
        self.types = True

class Car :
    def __init__(self,eng = None,acc = None ,brk = None ):
        self.eng = eng
        self.acc = True
        self.brk = False

    def start_the_car(self):
        self.brk = True
        self.acc = True
        self.eng.toStart()


class Engine :
    
    def __init__(self,piston = None,types = None):
        self.piston = False
        self.types = False
    
    
    def toStart(self):
        self.piston = True
        self.types = True

class Car :
    def __init__(self,eng = None,acc = None ,brk = None ):
        self.eng = eng
        self.acc = True
        self.brk = False

    def start_the_car(self):
        self.brk = True
        self.acc = True
        self.eng.toStart()


v8 = Engine()
bmw = Car(eng = v8)

bmw.start_the_car()


