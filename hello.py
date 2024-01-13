#simple hello world code
print("hello world")

#variable declaration 
myNumber = 100
print(myNumber)
myNumber = 'a'
print(myNumber)
myNumber = "hello-world"
print(myNumber)
myNumber = True
print(myNumber)

#creataing list
myList = []
myList.append(100)
myList.append('a')
myList.append("hello")
myList.append(234)

print(myList)

#creating dictionary
dict = []
dict = {1: "kalyani", 2: "it-vedant", 3: "mumbai"}

print(dict)

#creating set : doesnot allow to fill duplicate values
mySet = set(["hey", "all", "welcome", "to", "it-vedant", "to", "join", "say", "hello", "all"])

print(mySet)

#creating tuples
tup = ("kalyani", "itvedant", "mumbai", "mumbai-72")

print(tup)

#input and output
name = input("Enter your name :")
print(name)

num1 = int(input("Enter num1 : "))
num2 = int(input("Enter num2 : "))
result = num1 + num2
print(num1 + num2)

result = num1 - num2
print(result)

result = num1 * num2
print(result)

result = num1 / num2
print(result)

result = num1 % num2
print(result)

#conditional statements
num3 = 4
if(num3 % 2 == 0):
    print("Even number ", num3)
else:
    print("Odd number ", num3) 


#defining functions 
def hello():
    print("hello all")

hello()

def addition(n1, n2):
    return n1 + n2

resultAddition = addition(3, 4)
print(resultAddition)

#defining functions with main function
def areaOfCircle(radius):
    return 3.14 * radius * radius

def Main():
    print("started")
    output = areaOfCircle(2)
    print(output)

if __name__=="__main__":
    Main()

#loop demo 
for step in range(7):  #by default the range starts with 0
    print("hello : ", step)

#module import demo
import math

def Main():
    num4 = -80
    print(num4)

    print(math.fabs(num4))

if __name__=="__main__":
    Main()