from LinkList import Link_list

class main :
    mylist = Link_list()

    for i in range (1 , 11) :
        mylist.addLast(i)

    mylist.showList()

    mylist.setAt(98,10)
    mylist.setAt(33,3)

    mylist.showList()

    print("this is the data on given index : ",mylist.getFrom(10))

    mylist.sortDesc()
    mylist.showList()

