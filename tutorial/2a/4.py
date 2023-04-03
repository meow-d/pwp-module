# input
print("Enter score: ", end="")
while True:
    try:
        score = int(input())
    except:
        print("Please input a number: ", end="")
    else:
        if score > 100 or score < 0:
            print("Please input a number between 0 and 100: ", end="")
        else:
            break

# score check
passed = True
if score >= 80:
    grade = "A"
elif score >= 70:
    grade = "B"
elif score >= 60:
    grade = "C"
elif score >= 50:
    grade = "D"
else:
    grade = "F"
    passed = False

# print results
if passed:
    print(f"Your grade is: {grade}, and you passed, congrats sweetie <3.")
else:
    print(f"Your grade is: {grade}, and you failed ahahahAHAHAAHAHAH what a loser.")
