#working with files 
#1. opening a file
#with open("my-file1.txt", "r") as file:                                    # relative path
with open("C:\KalyaniDinde\Python\my-files\my-file1.txt", "r") as file:     # absolute path
    print("file opened")

#2. reading from file
#2.a reading single line from file
with open("C:\KalyaniDinde\Python\my-files\my-file1.txt", "r") as file:     # absolute path
    print("file opened")
    file_content = file.readline()                                          # reading single line    

print(file_content)

#2.b reading all the file
with open("C:\KalyaniDinde\Python\my-files\my-file1.txt", "r") as file:     
    print("file opened")
    file_content = file.read()                                              # reading entire file

print(file_content)

#2.c reading lines from file
with open("C:\KalyaniDinde\Python\my-files\my-file1.txt", "r") as file:
    print("file opened")
    file_content = file.readlines()                                         # reading file content line wise
                                                                            # and return a list
print(file_content)

#3. writing to file
with open("C:\KalyaniDinde\Python\my-files\my-file1.txt", "w") as file:
    print("file opened")
    file.write("This is IT-Vedant Pvt. Ltd., Mumbai")                       # writing content to file

print("file written")

#4. appending to file
with open("C:\KalyaniDinde\Python\my-files\my-file1.txt", "a") as file:
    print("file opened")
    file.write("This is python session")

print("file appended")