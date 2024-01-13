# simple class and object example 
class Person:
    name = "kalyani"
    age = 30
    email = "kas@gmail.com"

    def display(self):
        print("Person name : ", self.name, ", age : ", self.age, ", email id : ", self.email)


p = Person()
p.display()

# simple class and object with user input -> accept() and display() function
class Employee:
    empno = 101
    ename = "kalyani"
    job = "trainer"
    salary = 20000
    dept = "eclass"

    def accept(self):
        print("Enter Employee details :")
        self.ename = input("Enter name : ")
        self.empno = int(input("Enter empno : "))
        selfjob = input("Enter job : ")
        self.salary = int(input("Enter salary : "))
        self.dept = int(input("Enter dept : "))

        #ename = input("Enter name : ")
        #empno = int(input("Enter empno : "))
        #job = input("Enter job : ")
        #salary = int(input("Enter salary : "))
        #dept = int(input("Enter dept : "))

    def display(self):
        print(" ***** Employee Information ***** ")
        print("Empno : ", self.empno)
        print("Ename : ", self.ename)
        print("Job : ", self.job)
        print("Salary : ", self.salary)
        print("Dept : ", self.dept)

emp = Employee()
emp.accept()
emp.display()

#simple class with constructor and methods display
class Student:
    name = ""
    rollno = 0
    dept = ""
    email = ""

    def __init__(self, name, rollno, dept, email):          #parametrized constructor
        self.name = name
        self.rollno = rollno
        self.dept = dept
        self.email = email

    def display(self):
        print(" ***** Student Information ***** ")
        print("Name : ", self.name)
        print("Rollno. : ", self.rollno)
        print("Department : ", self.dept)
        print("Email ID : ", self.email)


stud = Student("deepika", 11, "mca", "deeps@gmail.com")
stud.display()

#class-object and constructor-destructor example 
class Person1:
    def __init__(self):                     # default/no-arg constructor
        self.user_name = "it-vedant"
        self.user_email = "itvedant2023@gmail.com"
        print("Name : ", self.user_name, ", Email : ", self.user_email)

    def __del__(self):                      # destructor demo
        print("Object destructed")

person = Person1()
del person
