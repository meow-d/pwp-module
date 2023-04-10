def main():
    number_1 = int(input("input the first number: "))
    number_2 = int(input("input the second number: "))
    print("1 = addition, 2 = subtraction, 3 = multiplication, 4 = division, 5 = power")
    operation = int(input("Choose your desired operation: "))

    if operation == 1:
        print(f"{number_1} plus {number_2} equals {number_1 + number_2}")
    elif operation == 2:
        print(f"{number_1} minus {number_2} equals {number_1 - number_2}")
    elif operation == 3:
        print(f"{number_1} times {number_2} equals {number_1 * number_2}")
    elif operation == 4:
        print(f"{number_1} divided by {number_2} equals {number_1 / number_2}")
    elif operation == 5:
        print(f"{number_1} to the power of {number_2} equals {number_1**number_2}")
    else:
        print("unknown operation, please input a number from 1 to 5")

if __name__ == "__main__":
    main()
