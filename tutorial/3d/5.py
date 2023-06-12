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
    number_of_students = input_but_convert_to_int("input number of students: ")
    student_scores = []

    for i in range(number_of_students):
        user_input = input(f"input score of {i+1}th student: ")
        student_scores.append(user_input)

    average_score = int(sum(student_scores) / number_of_students)
    print(f"average score is {average_score}")


if __name__ == "__main__":
    main()
