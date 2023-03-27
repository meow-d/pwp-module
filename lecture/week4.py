
def q1():
    i = 1
    while i <= 20:
        print(i)
        i = i + 1
    print()

def q2():
    i = 1
    while i <= 20:
        print(i * i)
        i = i + 1
    print()

def q4():
    i = 1
    while i <= 20:
        print(i * i * i)
        i = i + 1
    print()

def cal_average(num_list):
    sum_num = 0
    for t in num_list:
        sum_num = sum_num + t[1]

    avg = sum_num / len(num_list)
    return avg

def q3():
    # random test data
    # students = [
    #     ["stuenslf", 1],
    #     ["stslf", 20],
    #     ["qqewq", 90],
    #     ["rdfsadjfosdjf", 30],
    #     ["rdfsadjfosdjf", 312],
    #     ["rdfsadjfosdjf", 20],
    #     ["rdfsadjfosdjf", 76],
    #     ["rdfsadjfosdjf", 86],
    #     ["rdfsadjfosdjf", 45],
    #     ["rdfsadjfosdaf", 96],
    # ]

    students = []
    i = 0
    while i < 9:
        students.append(list())
        print("please input name for student " + str(i))
        students[i].append(input())
        print("please input marks for student " + str(i))
        while True:
            try:
                students[i].append(int(input()))
            except ValueError:
                print("please input a number")
            else:
                break
        i = i + 1
        print()
    average_marks = cal_average(students)
    print (average_marks)

def main():
    q1()
    q2()
    q3()
    q4()

if __name__ == "__main__":
    main()
