def input_but_convert_to_int(input_text: str):
    while True:
        user_input = input(input_text)
        try:
            user_input = int(user_input)
        except:
            print("please input a number.")
        else:
            break
    return user_input


def main():
    student_name = input("Enter the student's name: ")
    student_tp_number = input("Enter the student's TP number: ")
    student_subject_marks = []

    for i in range(5):
        user_input = input_but_convert_to_int(f"enter the marks for subject {i+1}: ")
        student_subject_marks.append(user_input)

    total_mark = sum(student_subject_marks)
    average_mark = sum(student_subject_marks) / len(student_subject_marks)
    if average_mark > 80:
        grade = "A"
    elif average_mark > 70:
        grade = "B"
    elif average_mark > 60:
        grade = "C"
    elif average_mark > 50:
        grade = "D"
    else:
        grade = "f"

    print(f"Student Name: {student_name}")
    print(f"TP Number: {student_tp_number}")
    print(f"Total Marks: {total_mark}")
    print(f"Average Mark: {average_mark}%")
    print(f"Grade: {grade}")


if __name__ == "__main__":
    main()
