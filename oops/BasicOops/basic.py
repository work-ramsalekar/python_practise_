
class Student :
   

    #one class have only one init method (constructors) if we declare the two init method, the init method which
    # are define last only this override all of the inint method

    ####### there are 3 main components of class  1) class level attribute
                                                 #2) object level attribute
                                                 #3) methods

    def __init__(self,name = None,age = None,marks = None):
        
        self.name=name
        self.age =age
        self.mark = marks

    def toString(self):
        print("the name is : ",self.name)
        print("the age is : ",self.age)
        print("the marks : ",self.mark)




st = Student("Ram",24,99)
st.toString()

st1 = Student()
