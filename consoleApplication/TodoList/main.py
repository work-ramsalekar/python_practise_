from item import Item 

class main :
    my_dict = {}
    end = False
    task_id = 5

    my_dict[1] = Item(1,"Gym","workout",False)
    my_dict[2] = Item(2,"tp","timepass",True)
    my_dict[3] = Item(3,"study","python",True)
    my_dict[4] = Item(4,"sql","ms-sql",False)

    while not end :
        print(
            ''' 
            0: exit
            1 : add new Task 
            2 : view all task
            3 : show all incomplete Task
            4 : show all completed Task
            '''
        )
        choose = int(input("Enter your choice : "))
        print()
        if(choose == 0) :
            end = True
            break

        elif(choose == 1):
            task = input("enter task name : ")
            desc = input("enter task descrption : ")
            my_dict[task_id] = Item(task_id,task,desc,False)
            task_id+=1

        elif(choose == 2):
            for task in my_dict :
                print(task , my_dict[task])
        
        elif(choose == 3):
            incompleted_tasks = list(filter(lambda x : x.status is not True , my_dict.values()))

            for tasks in incompleted_tasks :
                print(tasks)

        elif(choose == 4):
            completed_task = list(filter(lambda x : x.status is True,my_dict.values())

            for tasks in completed_task :
                print(tasks)
            