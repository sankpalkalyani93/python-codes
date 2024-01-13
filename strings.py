#strings demo
data = 'y'
fruit = 'apple'
city = "nashik"
address = """Pareirawadi, sakinaka, mumbai-72"""

print(data)
print(fruit)
print(city)
print(address)

#reading string characters index-wise
company = "It-Vedant Private Ltd."
print(company[1], " : ", company[12], " : ", company[-1], " : ", company[-12])

#string slicing
name = "kalyani-sankpal-dinde"
print(name[3:12])
print(name[12:-5])

#reversing string
name2 = "kalyani akash dinde"
print(name[::-1])
print("".join(reversed(name2)))

#updating string
message = "welcome to python session"
print("Original message string : ", message)

message = "Hey all, welcome to python session"
print("Updated message string : ", message)

#deleting character from string : strings are imutable, we cannot delete characters from string
message1 = "Hello all"
print("Original message1 string : ", message1)

#-------------------------------------------------------------------------------------------------------------
#del(message1[3])
#print("After deletion message1 string : ", message1) #TypeError: 'str' object doesn't support item deletion
#-------------------------------------------------------------------------------------------------------------

#using slicing to delete character and storing string in new string
message2 = "hello there, i am a trainer"
print("Original message2 string : ", message2)

message3 = message2[0:13] + message2[15:]
print("After deletion message3 string : ", message3)

#deleting complete string
message4 = "Welcome to python session"
print("Original message4 string : ", message4)

del(message4)
print("message4 after deletion : ", message4)   #Original message4 string :  Welcome to python session
                                                #Traceback (most recent call last):
                                                #File "C:\KalyaniDinde\Python\strings.py", line 54, in <module>
                                                #print("message4 after deletion : ", message4)
                                                #                                   ^^^^^^^^
                                                #NameError: name 'message4' is not defined. Did you mean: 'message'?

                                                