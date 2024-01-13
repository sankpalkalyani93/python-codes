import os

#1. Copy content from one file and paste in another file using file functions?
with open("C:\KalyaniDinde\Python\my-files\my-file1.txt", "r") as file1:
    content_to_write = file1.read()        
    file1.close()

with open("C:\KalyaniDinde\Python\my-files\my-file3.txt", "w") as file2:
    file2.write(content_to_write)
    print("file content copied")
    file2.close()   
#----------------------------------------------------------------------------------------------------------------

#2. Explain serialization and deserialization with examples
import pickle
data = {"name": "kalyani", "age": 30}

with open("C:\KalyaniDinde\Python\my-files\my-file4.pickle", "wb") as file4:
    pickle.dump(data, file4)
    print("file serialized")
    file4.close()

with open("C:\KalyaniDinde\Python\my-files\my-file4.pickle", "rb") as file4:
    #read_serialized_data = file4.read()                                        #reads data in serialized form
    #print(read_serialized_data)
    read_serialized_data = pickle.load(file4)
    print(read_serialized_data)
    file4.close()

#----------------------------------------------------------------------------------------------------------------

#3. What is file? What are the different modes of file?
#ans. A "file" refers to a named location on a storage device (e.g., a hard drive) that stores data in a 
# structured or unstructured format. Files are used to store and manage data that can be read from and 
# written to by programs. Python provides built-in functions and modules for working with files, allowing
# us to perform operations like reading, writing, and manipulating data stored in files.

#3.1 File Types:
# Files in Python can be of various types, including text files, binary files, and special file types like 
# CSV files, JSON files, XML files, and more. Text files contain human-readable text and are often used for
# configuration files, source code, and plain text documents. Binary files contain non-text data and can 
# store a wide range of information, such as images, audio, video, and compiled code.

#3.2 File Modes:
# When working with files in Python, you specify a file mode that determines how you can interact with 
# the file. Common file modes include:
    #1. "r": Read (default mode) - Allows reading the file.
    #2. "w": Write - Allows writing to the file (creates a new file or truncates an existing one). 
    #3. "a": Append - Allows appending data to the end of the file.
    #4. "rb" and "wb": Binary read and write modes for working with binary files.
    #5. "x": Exclusive creation - Creates a new file but raises an error if the file already exists.

#3.3 File Operations:
# Python provides functions and methods for various file operations, such as open() for opening files, 
# read() for reading data from files, write() for writing data to files, and close() for closing files.
# We can also use context managers (e.g., with open(...) as ...) to automatically manage file handling 
# and ensure proper file closure.

#3.5 File Paths:
# File paths specify the location of a file on the filesystem. They can be absolute (e.g., "/path/to/file")
# or relative to the current working directory (e.g., "file.txt"). Python's os and os.path modules provide
# functions for working with file paths, including joining, splitting, and checking file existence.

#3.6 Error Handling:
# When working with files, it's essential to handle exceptions, such as FileNotFoundError and PermissionError,
# to deal with issues like missing files or insufficient permissions.

#3.7 Serialization:
# Serialization refers to the process of converting Python data structures into a format that can be 
# saved to a file and later loaded and reconstructed. Common serialization formats include JSON, pickle,
# and XML.

#----------------------------------------------------------------------------------------------------------------

#4. Consider the file test.txt and perform following operations
    #1. open the file if exists, if not create  a new file

file_name = "C:\KalyaniDinde\Python\my-files\my-file2.txt"
if os.path.exists(file_name):
    print("file already existing")
else:
    print("file does not exist")
    with open("C:\KalyaniDinde\Python\my-files\my-file2.txt", "w") as file:
        print("file created/opened")
        file.close()

    #2. add string 'abcde' to the end of the file
with open("C:\KalyaniDinde\Python\my-files\my-file2.txt", "w") as file:        
        file.write("abcde")
        print("file written")
        file.close()

    #3. read and display first 5 characters
with open("C:\KalyaniDinde\Python\my-files\my-file2.txt", "r") as file:
    str = file.read(5)
    print(str)
    file.close()

    #4. display total number of characters present in the file
with open("C:\KalyaniDinde\Python\my-files\my-file2.txt", "r") as file:
    str = file.read()
    print(str, len(str))