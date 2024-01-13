#list
data1 = ['a', "hello", "hiii", "welcome", "hello", 422003, False, 100+35]
print(data1)
data1.append("list-demo")
print(data1)
print(data1.count('hello'))
data1.pop()
print(data1)
data2 = data1.copy()
print("data2 list : ", data2)
data1.insert(3, "kalyani")
print(data1)
data1.reverse()
print("data1 list --> ", data1)
    #data1.remove("hola")  ---> error as value not in list
data1.remove("welcome")
print(data1)
data2.clear()
print("data2 list --> ", data2)
print("element at 4th index of data1 : ", data1[4])
print("--------------------------")
for i in data1:
    print(i)
print("--------------------------")

#tuple 
tuple = (1, "apple", " : ", 2, "banana")
print(tuple)
print(tuple[4])
x = tuple.count("apple")
print("x --> ", x)
print(tuple.index("apple"))
print(tuple.index(1))
print(tuple.index(" : "))

print("--------------------------")
i = 0
while i < 5:
    print(tuple[i])
    i=i+1
print("--------------------------")

#set


#dictionary 
dictionary = dict()
dictionary[100] = "nashik"
dictionary[101] = "pune"
dictionary[102] = "mumbai"
dictionary[103] = "nagpur"
dictionary[105] = "kolhapur"

print(dictionary)
print(dictionary.keys())
print(dictionary.values())

for i in dictionary:
    print(i, " : ", dictionary[i])

print("104" in dictionary)
print(103 in dictionary)

del dictionary[102]
print(dictionary)

print(str(dictionary))
print(dictionary.items())

print(len(dictionary))
print(type(dictionary))

dictTemp = {}
dictTemp = dictionary.copy()
print("dictTemp --> ", dictTemp)

dictionary.clear()
print("dictionary after applying clear() : ", dictionary.items())

dict1 = {}  #empty dictionary
print("dict1 : ", dict1)

dict2 = dict()  #empty dictionary
print("dict2 : ", dict2)

dict3 = dict({1: "apple", 2 : "banana", 3 : "kiwi"})    #dict() with keys+values
print("dict3 : ", dict3)

dict4 = dict([(1, "apple"), (2, "banana"), (3, "mango")])   #dict() having each item as pair
print(dict4)

#nested dictionary
dict5 = {1: "hello", 2: "all", 3: "welcome to", 4: {'a': "it-vedant", 'b': "mumbai", 'c': "java-full-stack"}}
print("dict5 : ", dict5)

#adding set of values to single key 
dict1[0] = "harry"          
dict1[1] = "ron"
dict1[2] = "hermoine"
dict1[3] = 'best', 'friends', 'forever' # set of values  
print("dict1 : ", dict1)