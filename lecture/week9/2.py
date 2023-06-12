from math import floor

str1 = "JohnDipPete"
str2 = "JaSonAy"


def print_middle_three_char(string: str):
    middle_of_string = floor(len(string) / 2)
    print(string[middle_of_string - 1 : middle_of_string + 2])


print_middle_three_char(str1)
print_middle_three_char(str2)
