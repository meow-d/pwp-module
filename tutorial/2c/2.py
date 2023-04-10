student_name = []
student_score = []
looping = True

while looping:
    student_name.append(input("input student name: "))
    while True:
        current_student_score = input("input exam score: ")
        try:
            current_student_score = int(current_student_score)
        except:
            print("Please input a number")
        else:
            if student_name[-1] == "" and current_student_score == 999:
                student_score.append(current_student_score)
                looping = False
                break
            elif (current_student_score > 100) or (current_student_score < 0):
                print("Please input a number between 0 to 100")
            else:
                student_score.append(current_student_score)
                break
    print()

print("average:", sum(student_score[:-1]) / len(student_score))
