#polymorphism in different classes
class India:
    def capital(self):
        print("Capital of India is New Delhi")

    def language(self):
        print("Indian's speak Hindi as their national language")

    def type(self):
        print("India is a sub-continent in Asia")

class USA:
    def capital(self):
        print("Capital of USA is Washington DC")

    def language(self):
        print("American's speak English as their natioanl language") 

    def type(self):
        print("USA is a continent in itself")

# We create a for loop that iterates through a tuple of objects. 
# Then call the methods without being concerned about which class type each object is. 
# We assume that these methods actually exist in each class. 

#class China: 
#    pass

india = India()
usa = USA()
#china = China()     # China has no capital/language/type member 
                    # this will generate error

#for country in (india, usa, china):
for country in (india, usa):
    country.capital()
    country.language()
    country.type()


# polymorphism in same class   
# for this we need to install multipledispatch
# pip3 install multipledispatch
from multipledispatch import dispatch

class Addition:
    @dispatch(int, float)
    def add(n1, n2):
        result = n1 + n2
        print("Addition 1 : ", result)

    @dispatch(str, str)
    def add(str1, str2):
        result = str1 + str2
        print("Addition 2 : ", result)

    @dispatch(int, float, float)
    def add(n1, n2, n3):
        result = n1 + n2 + n3
        print("Addition 3 : ", result)

addition = Addition()
n1 = int(input("Enter value for n1 : "))
n2 = float(input("Enter value for n2 : "))
addition.add(n1, n2)

str1 = input("Enter message 1 : ")
str2 = input("Enter message 2 : ")
addition.add(str1, str2)

n3 = (float(input("Enter value for n3 : ")))
addition.add(n1, n2, n3)

#polymorphism with inheritance
class Animal(object):
    def speak(self):
        return "sound...!"

class Dog(Animal):
    def speak(self):
        #print("I woof")
        return "woof"

class Cat(Animal):
    def speak(self):
        #print("I meow")
        return "meow"

cat = Cat()
print("CAT : ", cat.speak())

dog = Dog()
print("DOG : ", dog.speak())

ant = Animal()
print("ANT : ", ant.speak())

