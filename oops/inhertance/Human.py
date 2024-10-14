class Living :
    def walk(slef):
        pass


class animal(Living):
    def walk(slef):
        print("Can Walk")


class plants(Living):
    def walk(slef):
        print("cannot move")




class main :
    dog =animal()
    dog.walk()

    rosePlant = plants()
    rosePlant.walk() 


    print(issubclass(plants,Living))
    print(issubclass(animal,Living))
    print(isinstance(dog, Living))