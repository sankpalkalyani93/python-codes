#inheritance demo -> single level
class Person:

    def __init__(self, name, empno):
        self.name = name
        self.empno = empno

    def display(self):
        print(self.name, " : ", self.empno)

p1 = Person("kalyani", 101)
p1.display()

class Employee(Person):
    def show(self):
        print("Employee class called")

emp = Employee("kalyani", 104)
emp.display()
emp.show()

#multilevel inheritance demo 
class Person1:
    def __init__(self, name):
        self.name = name

    def show1(self):
        print("Person1 : ", self.name)

class Employee1(Person1):
    def __init__(self, name, empno):
        Person1.__init__(self, name)
        self.empno = empno

    def show2(self):
        print("Employee1 : ", self.empno)

class Worker1(Employee1):
    def __init__(self, name, empno, wage):
        Employee1.__init__(self, name, empno)
        self.wage = wage

    def show3(self):
        print("Worker1 wage : ", self.wage)

w1 = Worker1("shrikant", 100, 23456)
w1.show1()
w1.show2()
w1.show3()        


# Multiple Inheritance 
class Base1(object):
    def __init__(self, num1):
        self.num1 = num1

    def getNum1(self):
        return self.num1

class Base2(object):
    def __init__(self, num2):
        self.num2 = num2

    def getNum2(self):
        return self.num2 
    
class Addition(Base1, Base2):
    
    def addition(self, Base1, Base2):
        self.n1 = Base1.getNum1() 
        self.n2 = Base2.getNum2()
        self.result = self.n1 + self.n2
        print("Result of addition : ", self.result)

add = Addition()
#add.addition()
# Hierarchical Inheritance


# Hybrid Inheritance