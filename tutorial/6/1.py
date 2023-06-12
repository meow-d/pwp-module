def main():
    data = [
        [
            "flight number",
            "departure time",
            "arrival time",
            "departure airport",
            "destination",
        ]
    ]

    data = read_csv_into_list()
    menu(data)
    write_list_into_csv(data)


def menu(data):
    while True:
        user_input = input(
            """
Options:
    1 = add data
    2 = view all data
    3 = search data
    0 = exit
Select an option: """
        )
        if user_input == "1":
            add_data(data)
        elif user_input == "2":
            view_all_data(data)
        elif user_input == "3":
            search_data(data)
        elif user_input == "0":
            break


def add_data(data):
    data.append([])
    for column_name in data[0]:
        user_input = input(f"Enter {column_name}: ")
        data[-1].append(user_input)


def view_all_data(data):
    print_data(data)


def search_data(data):
    result_data = [data[0]]

    search_string = input("Enter search string: ")
    for row in data[1:]:
        for field in row:
            if search_string in field:
                result_data.append(row)

    if len(result_data) == 1:
        print("\nNo results found.")
    else:
        print("\nResults:")
        print_data(result_data)


def print_data(data):
    text_to_print = ""

    for value in data[0]:
        text_to_print += value + "|"
    print("|" + text_to_print)

    for row in data[1:]:
        text_to_print = ""
        for value in row:
            text_to_print += value + "|"
        print("|" + text_to_print)


def write_list_into_csv(data):
    csv_text_data = ""
    for row in data:
        csv_text_data += ",".join(row) + "\n"
    try:
        open("data.txt", "x")
    except:
        pass
    with open("data.txt", "w") as file:
        file.write(csv_text_data)


def read_csv_into_list() -> list:
    out = []
    with open("data.txt", "r") as file:
        asodjfoaj_i_hate_naming_variables = file.read().splitlines()
    for line in asodjfoaj_i_hate_naming_variables:
        out.append(line.split(","))
    return out


if __name__ == "__main__":
    main()
