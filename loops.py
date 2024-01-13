#printing elements of list
x = [1, 2]
y = [4, 5]

for i in x:
    print(i)
    for j in y:
        print(j)


#printing table of a number
for i in range(2,4):
    for j in range(1, 11):
        print(i, " * ", j, " = ", i*j)

#printing row and col
for row in range(1, 3):
    for col in range(1, 3):
        print(row, " : ", col)


# for and while combo
list1 = ["I am", "You are"]
list2 = ["happy", "a believer", "fine"]

list2Size = len(list2)

for item in list1:
    i = 0

    while (i < list2Size):
        print(item, list2[i])
        i += 1

#using break inside loop
for i in range(2, 4):
    for j in range(1, 11):
        if (i==j):
            break
            
        print(i, " * ", j, " = ", i*j)

#using continue inside loop
for i in range(2, 4):
    for j in range(1, 11):
        if (i == j):
            continue

        print(i, " * ", j, " = ", i*j)