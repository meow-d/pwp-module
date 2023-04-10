def input_int(input_text):
    while True:
        current_input = input(input_text)
        try:
            current_input = int(current_input)
        except:
            print("Please input a number")
        else:
            return current_input


def check_marks(thing_to_check: str, minimum_mark: int):
    current_checking_mark = input_int(f"Enter your {thing_to_check} marks: ")
    if current_checking_mark < minimum_mark:
        print(f"Please retake your {thing_to_check}\n")
        return True


def main():
    while True:
        if check_marks("assignment", 25):
            continue
        if check_marks("test", 25):
            continue
        if check_marks("exam", 50):
            continue
        print("Congratulations, you have passed the module!\n")


if __name__ == "__main__":
    main()
