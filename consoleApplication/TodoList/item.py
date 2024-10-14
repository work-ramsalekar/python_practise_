class Item :
    def __init__(self,id,task,desc,status) :
        self.id = id
        self.task = task
        self.desc = desc
        self.status = status

    def __str__(self) -> str :
        return f"{self.task} and its status : {self.status}"
    
    def __hash__(self) -> int:
        return hash((self.id , self.task))
    
    def __eq__(self, value: object) -> bool:
        if not isinstance(value,Item) :
            return False
        return self.id == value.id and self.task == value.task