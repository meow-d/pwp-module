student_name = input("Please enter the student's name: ")
student_marks = int(input("Please enter the student's marks: "))

if student_marks > 50:
    print(f"Congratulations {student_name}, you have passed the exam!")
else:
    print(f"Congratulations {student_name}, you're a dissapointment!")
