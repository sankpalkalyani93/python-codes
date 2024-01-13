import array as arr
a = arr.array('i', [10, 20, 30, 40, 50])
print(a[0])
print(a[1])
print(a[2])
print(a[3])
print(a[4])
print(a[-1])
print(a[-2])
print(a[-3])
print(a[-4])
print(a[-5])

numbers = arr.array("i", [1, 2, 3, 4, 5, 6, 7, 8])
#changing first element by value 0
numbers[0] = 0
print(numbers)

numbers[5] = 100
print(numbers)

numbers[2:5] = arr.array("i", [101, 102, 103])
print(numbers)

#deleting element from array
del numbers[2]
print(numbers)

#finding length of array
x = len(numbers) 
print(x)

#concatenating arrays
a1 = arr.array("i", [1, 2, 3, 4, 5])
#a2 = arr.array("i", ['a', 'b', 'c', 'd'])  #TypeError: 'str' object cannot be interpreted as an integer
#a2 = arr.array("i", [6.1, 7.2, 8.3, 9.4, 10.5]) #TypeError: 'float' object cannot be interpreted as an integer
a2 = arr.array("i", [6, 7, 8, 9, 10])
a3 = arr.array("i")
a3 = a1 + a2
print(a3)

jobs = arr.array("u", ['trainer', 'doctor', 'teacher', 'painter'])
cities = arr.array("u", ['nashik', 'mumbai', 'pune'])
totalData = arr.array("u")
totalData = jobs + cities
print(totalData)