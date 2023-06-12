# the question is really really unclear on what to do so i'm not even following it now


def main():
    student_data = [["student name", "student TP number", "amount of subjects"]]
    user_interface(student_data)


def user_interface(student_data):
    while True:
        continue_program = input(
            "Do you want to continue? ‘0’ to Continue ‘-1’ to Terminate: "
        )
        if continue_program == "0":
            pass
        elif continue_program == "-1":
            break
        else:
            print("unknown input, continuing")

        option = input(
            """\nYour Options are
    1.Add new student detail.
    2.View all student details.
    3.Search Specific student detail.
Select an option:"""
        )
        if option == "1":
            add_new_student(student_data)
        elif option == "2":
            display(student_data)
        elif option == "3":
            search_student_data(student_data)
        else:
            print("unknown input, continuing")


def add_new_student(student_data):
    student_data.append([])

    for column in student_data[0]:
        user_input = input(f"Enter {column}: ")
        student_data[-1].append(user_input)

    i = int(student_data[-1][2])
    j = int(student_data[-1][2])
    while i != 0:
        user_input = int(input(f"Enter marks for subject {j-i+1}: "))
        student_data[-1].append(user_input)
        i -= 1

    print(student_data[-1][3:])
    total_marks = sum(student_data[-1][3:])
    average_marks = average(student_data[-1][3:])
    student_grade = grade(average_marks)
    print(f"Total of all subjects: {total_marks}")
    print(f"Average: {average_marks}")
    print(f"Grade: {student_grade}")


def display(student_data):
    for row in student_data:
        print(", ".join(row))


def search_student_data(student_data):
    search_string = input("Search student details:")
    result_count = 0
    results = ""
    for row in student_data[1:]:
        if search_string in row[0]:
            results += ", ".join(row) + "\n"
            result_count += 1
    if result_count == 0:
        print("No students found")
    else:
        print(f"{result_count} students found:")
        print(results)


def average(number_list: list[int | float]):
    return sum(number_list) / len(number_list)


def grade(score: int | float):
    if score >= 100:
        return "A+"
    elif score >= 80:
        return "A"
    elif score >= 75:
        return "A-"
    elif score >= 70:
        return "B+"
    elif score >= 65:
        return "B"
    elif score >= 60:
        return "C+"
    elif score >= 55:
        return "C"
    elif score >= 50:
        return "C-"
    elif score >= 0:
        return "D/Fail"
    else:
        return "Invalid score"


if __name__ == "__main__":
    main()
