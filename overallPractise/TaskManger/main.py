from utility import Utility
from Task import Task
class main :
    todolist = []
    todolist.append(Task(1,"Gym",False))
    todolist.append(Task(2,"Pyhon",True))
    todolist.append(Task(3,"Tp",True))
    taskId = 4

    end = False

    while(not end):
        print(
            '''
            0 : exit
            1 : add new Task
            2 : view all Task
            3 : do todolist
            4 : read from file  
            5 : list of all remaing tasks
            '''
        )
        choose = int(input("Enter the choose :   "))

        if(choose == 0):
                print("Thanks visit again")
                end = True
                break
        
        elif (choose == 1):
                TaskName = input("Enter the Task Name : ")
                todolist.append(Task(taskId,TaskName,False))
                taskId +=1
                
        
        elif(choose == 2):
              for tasks in todolist :
                    print(tasks)
                    
        elif(choose == 3):
              
            Utility.__writingWhole__(todolist)

        elif(choose == 4):
              print(Utility.__readingfromFile__())
        
        elif(choose == 5):
              for tasks in todolist:
                    if(not tasks.Status):
                          print(tasks)


        


   
    