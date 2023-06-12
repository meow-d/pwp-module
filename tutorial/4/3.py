def add(number1, number2):
    return number1 + number2


def subtract(number1, number2):
    return number1 - number2


def multiply(number1, number2):
    return number1 * number2


def divide(number1, number2):
    if number2 != 0:
        return number1 / number2


operation = int(
    int(input("select an operation (1=add, 2=subtract, 3=multiply, 4=divide): "))
)
number1 = int(input("input first number: "))
number2 = int(input("input second number: "))

result = "invalid operation"
operation_name = "invalid operation"
if operation == 1:
    result = add(number1, number2)
    operation_name = "sum"
elif operation == 2:
    result = subtract(number1, number2)
    operation_name = "difference"
elif operation == 3:
    result = multiply(number1, number2)
    operation_name = "product"
elif operation == 4:
    result = divide(number1, number2)
    operation_name = "quotient"

print(f"{operation_name} of {number1} and {number2} is {result}")
