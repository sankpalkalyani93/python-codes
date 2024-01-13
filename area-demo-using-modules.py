import area  # importing the custom made module

radius = int(input("Enter value for radius : "))
areaOfCircle = area.areaOfCircle(radius)
print("Area of circle : ", areaOfCircle)

base = int(input("Enter value for base : "))
height = int(input("Enter value for height : "))
areaOfTriangle = area.areaOfTriangle(base, height)
print("Area of Triangle : ", areaOfTriangle)