from node import node
class Link_list :
    def __init__(self):
        self.head = None
        self.size = 0

    def addLast(self,value):
        self.size +=1
        newNode = node(value)

        if not self.head :
            self.head = newNode
            return
        temp_node = self.head

        while temp_node.next:
            temp_node = temp_node.next
        temp_node.next = newNode

    def showList(self):
        if not self.head :
            print("it is empty list")
            return
        
        temp_node = self.head
        while temp_node :
            print(temp_node.data," -> ",end=" ")
            temp_node = temp_node.next
        print("null")

    def addFirst(self,value):
        self.size +=1
        newNode = node(value)

        if not self.head :
            self.head = newNode
            return
        
        newNode.next = self.head
        self.head = newNode

    def setAt(self,value,index) :
        
        

        if(index >= self.size) :
            print("index out of bound : ")
            return
        
        tempNode = self.head
        for n in range (0,index) :
            tempNode = tempNode.next

        tempNode.data = value

    def getFrom (self,index) -> int :
        

        if(index < 0 or index >= self.size):
            print("index out of bound ")
            return
        
        tempNode = self.head

        for i in range (index) :
            tempNode = tempNode.next
        return tempNode.data

    def sortDesc(self) :
        for i in range (1,self.size) :
            for j in range (i , self.size) :
                if(self.getFrom(j) > self.getFrom(i)) :
                    temp = self.getFrom(j)
                    self.setAt(self.getFrom(i),j)
                    self.setAt(temp,i)

    