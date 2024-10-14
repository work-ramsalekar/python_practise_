class items :
    def __init__(self,id : int,name : str,desc : str ,princ : int):
        self.id = id
        self.name = name
        self.desc = desc
        self.price = princ

    def __str__(self) -> str:
        return f"{self.id} : {self.name} and the price is : {self.price}"

    def __eq__(self, value: object) -> bool:
        if isinstance(value,items):
            return self.id == value.id
        return False

     