#1 --> Features of Python 
    #ans :  Python is a versatile and popular programming language known for its simplicity and readability. 
    #       It has a wide range of features that make it suitable for various applications. 
    #       Here are some key features of Python:
    #       1. Easy-to-Read         :   Python uses a clear and easy-to-read syntax, which emphasizes code readability. 
    #                                   This reduces the cost of program maintenance and development.
    #       2. High-Level           :   Python is a high-level language, which means it abstracts many low-level details,
    #                                   making it easier to write code and focus on solving problems.
    #       3. Interpreted          :   Python is an interpreted language, which means you can run code directly without
    #                                   the need for compilation. This makes development faster and more flexible.
    #       4. Cross-Platform       :   Python is available on various platforms, including Windows, macOS, and Linux. 
    #                                   You can write code on one platform and run it on another with minimal changes.
    #       5. Extensive Std.       :   Python has a rich standard library that provides modules and packages for a wide 
    #          Library                  range of tasks, from file handling to web development.
    #                                   This reduces the need to write code from scratch.
    #       6. Dynamic Typing       :   Python uses dynamic typing, which means you don't need to declare variable types
    #                                   explicitly. Python determines the data type of a variable at runtime.
    #       7. Object-Oriented      :   Python supports object-oriented programming (OOP) principles, allowing you to 
    #                                   create reusable and organized code using classes and objects.
    #       8. Interoperability     :   Python can easily integrate with other languages like C, C++, and Java, allowing
    #                                   you to leverage existing code and libraries.
    #       9. Community Support    :   Python has a large and active community of developers. You can find extensive 
    #                                   documentation, tutorials, and third-party libraries to solve a wide range of problems.
    #       10. Open Source         :   Python is an open-source language, which means it's free to use, modify, and distribute.
    #                                   This encourages collaboration and innovation.
    #       11. Versatile           :   Python is a multipurpose language used in web development, data science, machine 
    #                                   learning, scientific computing, scripting, automation, and more.
    #       12. Strong Ecosystem    :   Python has a robust ecosystem with popular frameworks and libraries like Django, 
    #                                   Flask, NumPy, Pandas, TensorFlow, and Matplotlib, which simplify various tasks.
    #       13. Read-Eval-Print 
    #           Loop (REPL)         :   Python provides a REPL environment, allowing you to experiment with code interactively
    #                                   and quickly test ideas.
    #       14. Garbage Collection  :   Python includes automatic memory management with a built-in garbage collector, reducing
    #                                   the risk of memory leaks.
    #       15. Concurrency Support :   Python supports various concurrency models, including multi-threading, multiprocessing,
    #                                   and asynchronous programming with asyncio.
    #       16. Community-Driven 
    #           Improvement         :   Python's development is guided by PEPs (Python Enhancement Proposals), 
    #                                   which are discussed and implemented through community consensus.
        
    #   These features, along with Python's simplicity and versatility, make it an excellent choice for 
    #   both beginners and experienced developers for a wide range of applications.

#2.1 --> Define Variable
    #ans :  In Python, a variable is a name that refers to a value or an object in memory. 
    #       Variables are used to store and manipulate data in your programs.
    #       1. Dynamic Typing   :   Python is dynamically typed, which means you don't need to declare the data type of a variable explicitly. 
    #                               The data type is determined automatically at runtime.
    #                               example : 
    #                               x = 10
    #                               name = "Alice"  
    #       2. Variable Names   :   Variable names can consist of letters (both uppercase and lowercase), digits, 
    #                               and underscores.
    #                               They must start with a letter (a-z, A-Z) or an underscore (_).
    #                               Variable names are case-sensitive, so myVar and myvar are considered different variables.
    #                               Python has reserved words (keywords) that you cannot use as variable names because they 
    #                               have special meanings in the language.
    #       3. Reassignment     :   You can change the value of a variable by assigning it a new value:        
    #                               example : 
    #                               x = 10
    #                               x = 5  (value of x is now 10)
    #       4. Variable Scope   :   Variables have a scope, which defines where they can be accessed or modified.
    #                               Variables defined within a function have local scope and are only accessible 
    #                               within that function.
    #                               Variables defined outside of any function (at the module level) have global 
    #                               scope and can be accessed throughout the module.
    #       5. Deleting Variables:  You can delete a variable using the del statement:
    #                               example :
    #                               x = 89
    #                               del x
    #       6. Multiple Assignment: Python allows you to assign multiple variables in a single line:
    #                               example :
    #                               x, y, z = 1, 2, 3
    #       7. Variable Interpolation: You can embed variable values within strings using f-strings (Python 3.6+):
    #                               example : 
    #                               name = "kalyani"
    #                               age = 30
    #                               email = "kas@gmail.com"
    #                               statement = f"My name is {name}, {age} years old and my email id is {email}"

#2.2 --> Difference betwween snake-case and camel case
    #ans    :   The key distinction between Snake-Case and Camel-Case is in how words are separated and capitalized:
    #           1. Snake case uses underscores and all lowercase letters(used for variables, functions, file names)
    #           example :   user_name = "kalyani"
    #                       user_age = 30
    #           2. Camel case doesn't use spaces or underscores and capitalizes the first letter of each word 
    #           (used for methods, class names)        
    #           example :   userName = "kalyani"
    #                        userAge = 30

#2.3 --> What is meant by integer division
    #ans    :   In Python, integer division (also known as floor division) is performed using the // operator. 
    #           It returns the floor value of the division result, which means it discards the fractional part 
    #           and returns the largest integer that is less than or equal to the result.  
    #           example :
num1 = 13
result = num1 // 3
print("floor or integer division : ", result)    


#2.4 --> Write program to exchange the values of two numbers with and without using temporary variables
    #ans    :   Swapping with third variable
x1 = 4
y1 = 5
print("Before swap \n x1 : ", x1, ", y1 : ", y1)
temp = x1
x1 = y1
y1 = temp
print("After swap \n x1 : ", x1, ", y1 : ", y1)

    #ans    :   Swapping without third variable
x2 = 3
y2 = 6
print("Before swap \n x2 : ", x2, ", y2 : ", y2)
x2 = x2 + y2
y2 = x2 - y2
x2 = x2 - y2
print("After swap by addition-subtraction logic \n x2 : ", x2, ", y2 : ", y2)
x2 = x2 * y2
y2 = x2 // y2
x2 = x2 // y2
print("After swap by multiplication-division logic \n x2 : ", x2, ", y2 : ", y2)

#2.5 --> Write a program to accept a string value via user input and display the same
    #ans    :   Consider the following example :
str = input("Enter a message of your choice : ") 
print(str)

#2.6 --> Write a program to find the average marks of three subjects
    #ans    :   consider the following example : 
m1 = int(input("Enter marks for subject 1 : "))
m2 = float(input("Enter marks for subject 2 : "))
m3 = float(input("Enter marks for subject 3 : "))
total = m1 + m2 + m3
avg = total / 3
print("Total : ", total, ", Avg : ", avg)

#3.1 --> Difference between high-level and low-level programming language
    #ans    :   
    #       a. High-Level Programming Language:
    #           1. Abstraction: High-level languages are designed with a high level of abstraction. 
    #           They provide programmers with a more abstracted and simplified view of the computer's hardware 
    #           and operations. This abstraction makes high-level languages easier to read, write, and 
    #           understand.

    #           2. Readability: Code written in high-level languages is typically more readable and closer to 
    #           human language. This makes it easier for programmers to express their ideas and algorithms 
    #           clearly.

    #           3. Portability: High-level languages are usually platform-independent or have better portability.
    #           Programs written in high-level languages can be executed on different platforms with minimal or 
    #           no modification.

    #           4. Productivity: High-level languages often come with a rich set of built-in functions and 
    #           libraries, which can significantly boost a programmer's productivity. These languages 
    #           simplify complex tasks and reduce the need for low-level memory management.

    #           5. Examples: Examples of high-level programming languages include Python, Java, C#, Ruby, 
    #           and JavaScript.

    #       b. Low-Level Programming Language:
    #           1. Abstraction: Low-level languages have a lower level of abstraction and are closer to the 
    #           hardware of the computer. Programmers have more direct control over the hardware, memory, and 
    #           system resources.

    #           2. Readability: Code written in low-level languages is less readable and more cryptic compared
    #           to high-level languages. It requires a deep understanding of hardware and system architecture.

    #           3. Portability: Programs written in low-level languages are often platform-dependent. 
    #           They may need to be rewritten or recompiled for different hardware or operating systems.

    #           4. Productivity: Low-level languages require more effort and time to write and debug code. 
    #           Programmers need to manage memory and hardware resources manually, which can be error-prone 
    #           and time-consuming.

    #           5. Examples: Examples of low-level programming languages include Assembly language, C, C++, 
    #           and Fortran.


#3.2 --> Describe python programming language
    #ans    :   Python is a high-level, interpreted, and versatile programming language known for its simplicity
    #           and readability. It was created by Guido van Rossum and first released in 1991. Python has gained
    #           widespread popularity in various fields, including web development, data science, machine learning
    #           , scientific computing, automation, and more. 
    #           Here are some key characteristics and features of Python:    
    #           1. Readability: Python emphasizes code readability and uses a clean and easy-to-read syntax, which
    #           makes it an excellent choice for beginners and experienced developers alike. Its indentation-based
    #           block structure enforces clean and consistent code formatting.

    #           2. High-Level Language: Python is a high-level programming language, which means it abstracts 
    #           many low-level details, making it easier to write code and focus on solving problems without 
    #           getting bogged down in system-specific details.

    #           3. Interpreted Language: Python is an interpreted language, which means you can write and run 
    #           code directly without the need for a separate compilation step. This results in a faster 
    #           development cycle.

    #           4. Cross-Platform: Python is available on various platforms, including Windows, macOS, Linux, 
    #           and others. This means you can write code on one platform and run it on another with minimal 
    #           modifications.

    #           5. Extensive Standard Library: Python comes with a comprehensive standard library that includes 
    #           modules and packages for various tasks, from file handling and networking to web development 
    #           and data analysis. This extensive library reduces the need to write code from scratch.

    #           6. Dynamic Typing: Python uses dynamic typing, where variable types are determined at runtime. 
    #           This allows for more flexible and concise code but requires attention to type compatibility.

    #           7. Object-Oriented: Python supports object-oriented programming (OOP) principles, allowing you 
    #           to create reusable and organized code using classes and objects.

    #           8. Large and Active Community: Python has a large and active community of developers. This 
    #           community contributes to the language's growth, maintains third-party libraries, and 
    #           provides extensive documentation and support.

    #           9. Versatility: Python is a multipurpose language used in various domains, including web 
    #           development (with frameworks like Django and Flask), data science (with libraries like NumPy 
    #           and Pandas), machine learning (with libraries like TensorFlow and PyTorch), 
    #           automation (with libraries like Selenium), and more.

    #           10. Open Source: Python is open-source and free to use, modify, and distribute. 
    #           This encourages collaboration and innovation.

    #           11. Garbage Collection: Python includes automatic memory management with a built-in garbage 
    #           collector, reducing the risk of memory leaks.

    #           12. Concurrent Programming Support: Python supports various concurrency models, including 
    #           multi-threading, multiprocessing, and asynchronous programming with asyncio.

    #           13. Interactive Environment: Python provides a Read-Eval-Print Loop (REPL) environment, 
    #           allowing you to experiment with code interactively and quickly test ideas.

    #           14. Community-Driven Development: Python's development is guided by Python Enhancement 
    #           Proposals (PEPs), which are discussed and implemented through community consensus.

#3.3 --> what is a platform independent language
    #ans    :   Python is often considered a platform-independent language due to several key features and 
    #           design choices:
    #           1. Interpreted Language: Python is an interpreted language, which means that it doesn't 
    #           require compilation into machine code for a specific platform. Instead, Python code is 
    #           executed by an interpreter that translates the code into machine instructions at runtime. 
    #           This interpretation allows Python programs to be executed on different platforms without 
    #           modification.

    #           2. Abstraction from Hardware: Python abstracts low-level details of hardware and operating 
    #           systems, providing a high-level interface to developers. This abstraction shields programmers 
    #           from dealing with platform-specific intricacies.

    #           3. Cross-Platform Compatibility: Python is available for various operating systems, 
    #           including Windows, macOS, Linux, and others. Python interpreters and standard libraries 
    #           are maintained to work consistently across these platforms, ensuring compatibility.

    #           4. Write Once, Run Anywhere: Python's platform independence is evident in the "write once, 
    #           run anywhere" philosophy. Code written in Python can often be used on multiple platforms 
    #           with little to no modification, making it a versatile choice for developers targeting 
    #           diverse environments.

    #           5. Standard Library and Third-Party Modules: Python's extensive standard library and numerous
    #           third-party libraries are designed to provide consistent functionality and behavior across 
    #           different platforms. This means that you can rely on these libraries when building any 
    #           cross-platform applications.

    #           6. Open Source Development: Python is an open-source language with a collaborative development
    #           model. The Python community actively works to ensure that Python remains compatible and 
    #           functional across various platforms. This community-driven approach helps maintain 
    #           platform independent nature.

    #           7. Virtual Environments: Python allows the creation of virtual environments, which are isolated 
    #           environments where you can install specific versions of Python packages and dependencies. 
    #           This isolation helps manage different projects with potentially conflicting dependencies and 
    #           ensures portability.

    #           8. Cross-Platform GUI Frameworks: Python has GUI frameworks like Tkinter, PyQt, and wxPython 
    #           that allow developers to create graphical user interfaces (GUIs) that can run on multiple 
    #           platforms.   

#4 --> write a command to check version of python on command proompt
    #ans    :   python --version
    #           python -V