def addition():
    x = 10
    y = 20
    result = x + y
    print("Result of addition : ", result)


addition()
    
def subtraction(x, y):
    return x - y

sub = subtraction(3, 4)
print("Subtraction result : ", sub)


def addition2():
    S = 0
    for i in range(10):
        S += i
        print(S)

    return S
    
print("Addition : ", addition2())