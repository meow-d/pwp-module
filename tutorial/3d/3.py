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
    number_of_students = input_but_convert_to_int("number of students: ")
    students = []

    for i in range(number_of_students):
        user_input = input(f"name of {i+1}th student: ")
        students.append(user_input)

    students = sorted(students)

    print("list of students: ")
    for i in students:
        print(i)


if __name__ == "__main__":
    main()
