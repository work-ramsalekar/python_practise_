class Task :
    def __init__(self,TaskId : int , TaskName : str , Status : bool ):
        self.TaskId= TaskId
        self.TaskName = TaskName
        self.Status = Status
    
    def __str__(self) -> str :
        return f"{self.TaskId} : {self.TaskName} and the status is : {self.Status}"
    
    