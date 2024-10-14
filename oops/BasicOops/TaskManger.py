


class Task :
    def __init__(self, title = None  , descrp = None , id = None):
        self.title = title
        self.id = id
        self.status = False
        self.desc = descrp

    def __str__(self) -> str:
         return f"id : {self.id} title : {self.title} status : {self.status}"

    def __eq__(self, other) -> bool:
        if isinstance(other,Task):
            return self.id == other.id and self.title == other.title
        else :
            return False


print("Welcome to todo application ")

end = False
todolist = []
todolist.append(Task("Gym","Do workouts",1))
todolist.append(Task("homework","do pending work",2))
todolist.append(Task("English","learn daily english",3))

while(not end):
    print('''
    0 : exit
    1 : add task
    2 : show all tasklist
    3 : mark done status by id
    ''')
    choose = int(input("Enter the choose : "))
    if(choose == 0):
        end = True
        print("Thanks start again ")
        break
    
    elif(choose == 1):
        taskid = 4
        taskName = input("Enter the task name : ")
        taskdec = input("Enter the descrption ")
        todolist.append(Task (taskName,taskdec,taskid ))
        taskid +=1

        print("add sucessfully")

    elif(choose == 2):
        print("The task list is : ")
        print()
        for tasks in todolist :
            print(tasks)
    
    elif(choose == 3):
        taskid = int(input("Enter id where to do done status "))
        for tasks in todolist :
             if(taskid == tasks.id):
                 tasks.status = True
        print("Done")

            
        
        
