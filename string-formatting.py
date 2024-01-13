#string formatting
string1 = "{} {} {}".format("its", "me", "kalyani")
print(string1)

string2 = "{1} {0} {2}".format("this", "is", "python")
print(string2)

string3 = "{w} {a} {h}".format(h="hello", a="and", w="welcome")
print(string3)

#formatting integers
string4 = "{0:b}".format(16)
print("binary representation of 16 : ", string4)

string5 = "{0:e}".format(165.6487)
print("exponent representation of 165.6487 : ", string5)

#string6 = "{0:2f}".format(1/6)     #0.166667
string6 = "{0:.2f}".format(1/6)     #0.17
print("one-sixth : ", string6)

#string alignment
string7 = "|{:<10}|{:^10}|{:>10}|".format('this', 'is', 'earth')
print(string7)

#aligning of spaces in string
string8 = "\n{0:^16} in the {1:<6}!".format("welcome to nashik", 2023)
print(string8)


