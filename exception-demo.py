#exception demo
result = 0
num = int(input("Enter value for num : "))
den = int(input("Enter value for den : "))
try: 
    result = num / den
    print("Result of division : ", result)
except:
    print("Exception : Division by 0.")  

#exception demo with array 
from array import *
a = array('i', [10, 20, 30, 40, 50])
index = int(input("Enter value for index : "))
den = int(input("Enter value for den : "))
try:
    result = a[index] / den
    print("Result of division : ", result)
except:
    print("Exception occurred")