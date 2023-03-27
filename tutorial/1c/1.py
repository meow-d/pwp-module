print("Enter score: ", end="")
score = int(input())

if score > 80:
    grade = "A"
elif score > 60:
    grade = "B"
elif score > 40:
    grade = "C"
else:
    grade = "D"

print("Your grade is:", grade)
