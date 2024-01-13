#fetching keyword list
import keyword

print(keyword.kwlist)

#understanding true, false and none
print(False == 0)
print(True == 1)

print(True + False + True)  # 1 + 0 + 1
print(False + True + False) # 0 + 1 + 1
print(False + False + False)# 0 + 0 + 0
print(True + True + True)   # 1 + 1 + 1

#understanding and, or, not, is, in
print(True and False)
print(False and True)

print((not False) and True and True)

if 's' in 'it-vedant, mumbai':
    print("s is available...")
else:
    print("s is not available")

for i in "kalyani-sankpal-dinde":
    print(i, end="-")

for i in range(10):
    print(i, end="->")

    if(i == 5):
        print("now we break...!")
        break


k = 1
while k < 10:
    #print("hello-all...!")

    if(k == 6):
        k += 1
        continue
    else:
        print(k, end="::")

    k += 1

x = 2
if(x % 2 == 0):
    print(x, " is divisible by 2")
elif(x % 5 == 0):
    print(x, " divisible by 5")
elif(x % 2 == 0 and x % 5 == 0):
    print(x, " is divisible by both 2 and 5")
else:
    print(x, " is not divisible by 2 and 5")