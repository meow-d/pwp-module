import math


def diameter(radius):
    return radius * 2


def circumference(radius):
    return 2 * math.pi * radius


def area(radius):
    return math.pi * math.sqrt(radius)


operation = int(
    int(input("select an operation (1=diameter, 2=circumference, 3=area): "))
)
radius = int(input("input the radius of the circle: "))

result = "invalid operation"
operation_name = "invalid operation"
if operation == 1:
    result = diameter(radius)
    operation_name = "diameter"
elif operation == 2:
    result = circumference(radius)
    operation_name = "circumference"
elif operation == 3:
    result = area(radius)
    operation_name = "area"

print(f"{operation_name} of {radius} is {result}")
