class Utility:
    content : str
     
    @staticmethod
    def __writingtoList__(con : str):
         
         print("SucessFully write")
         with open ("mytodolist.txt","w+") as f :
            f.append(con)
      
    @staticmethod
    def __writingWhole__(con : list):
        with open ("mytodolist.txt","w+") as f :
            for i in con :
                f.write(str(i) + '\n')
        print("write sucesfully") 

    @staticmethod
    def __readingfromFile__() -> str:
        print("the text from the file is :  ")
        with open("mytodolist.txt","r") as f :
            content = f.read()

        return content
 
    
      