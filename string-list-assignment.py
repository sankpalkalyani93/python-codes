#accept a string and display it by removing the vowels from it
str = "hello and welcome all"
vowels = "AEIOUaeiou"
result = ""

for char in str:
    if char not in vowels:
        result += char

print("Strign without vowels : " + result)

#accept a string and display all the vowels from it
str1 = "hello and welcoem all"
result1 = ""

for char in str1:
    if char in vowels:
        result1 += char

print("String containing vowels : " + result1)

#Write a program that creates a list of 10 random integers. Then create two lists by
#name odd_list and even_list that have all odd and even values of the list respectively.
numberList = [11, 13, 15, 17, 18, 7, 10, 20, 15, 18]
even = []
odd = []

for i in numberList:
    if i % 2 == 0:
        even.append(i)
    else:
        odd.append(i)

print("even list : ", even)
print("odd list : ", odd)

#Write a program that has the dictionary of your friends’ names as keys and phone
#numbers as its values. Print the dictionary in a sorted order. Prompt the user to
#enter the name and check if it is present in the dictionary. If the name is not present,
#then enter the details in the dictionary.
contact = dict({"shree": "1234567890", "deepika": "3214234567", "kalyani": "9867543210", "sham": "6545789812"})
print(contact)
flag = 0
name = input("Enter friend's name : ")
for n in contact:
    if n == name:
        #print("found --> ", n)
        flag = 1
        break

if flag == 1: 
    print("contact found")
else:
    print("contact not found", name)
    value = input("Enter your phone number: ")
    contact[name] = value

print(contact)


