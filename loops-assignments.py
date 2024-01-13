#1 Write a program to display the following pattern using nested loops.
# 1                     1
# 22                   21
# 333                 321
# 4444               4321
# 55555             54321

n = 1
num = 5
for i in range(1, num + 1):     
    for j in range(1, i + 1):
        print(i, end="")
        
    print()
    

rows = 6
for i in range(1, rows + 1):
    for j in range(rows, i, -1):
            print(" ", end=" ")
    for k in range(i, 0, -1): 
            print(k, end=" ")     
    print() 

#2 Write a program that uses a while loop to add up all the even numbers between 100 and 200.
sumOdd = 0
sumEven = 0
x = 100
while(x <= 200):
    if x % 2 == 0:
        sumEven += x
    else: 
        sumOdd += x
    x = x+1

print("Sum of even numbers : ", sumEven)
print("Sum of Odd numbers : ", sumOdd)

#3  write a program that receives 3 sets of values of p, n, and r and calculates simple interest for each
setLimit = int(input("Enter the limit of sets : "))
results = []

for i in range(setLimit):
    p = int(input("Enter value for p : "))
    n = int(input("Enter value for n : "))
    r = int(input("Enter value for r : "))
    
    simpleInterest = (p * n * r) // 100
    print("Simple Interest for ", i, " : ", simpleInterest)


#4 Write for code for while loop where a person is waiting for the Bus.
busArrived = False

while not busArrived:
    personStatus = input("Has the bus arrived ? Please answer in yes/no : ")
    if personStatus == "yes":
        print("Okay, You can now board the bus")
        busArrived = True
    elif personStatus == "no":
        print("Please wait for the bus, it is on its way.") 
    else:
        print("You have entered wrong input.")
    