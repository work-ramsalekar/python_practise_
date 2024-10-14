with open("Filehandlingbasic\hello.txt","+r") as filecontent :
    content = filecontent.read()

    print(content)

    filecontent.write("This is append new content ")

#content = filecontent.read()