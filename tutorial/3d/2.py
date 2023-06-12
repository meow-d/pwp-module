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
    list_size = input_but_convert_to_int("size of the list: ")
    my_list = []

    for i in range(list_size):
        user_input = input(f"input {i+1}th element: ")
        my_list.append(user_input)

    print(my_list)


if __name__ == "__main__":
    main()
