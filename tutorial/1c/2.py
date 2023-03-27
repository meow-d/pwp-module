restaurants = [
    ["Joe’s Gourmet Burgers", False, False, False],
    ["Main Street Pizza Company", True, False, True],
    ["Corner Café", True, True, True],
    ["Mama’s Fine Italian", True, False, False],
    ["The Chef’s Kitchen", True, True, True],
]
restaurant_criteria = [False]


def user_input():
    while True:
        response = input()
        if response == None:
            response = True
            break
        else:
            if response == "Y" or "y" or "yes" or "Yes":
                response = True
                break
            elif response == "N" or "n" or "No" or "no":
                response = False
                break
            else:
                print("please enter a valid answer:", end="")
    restaurant_criteria.append(response)


print("Is anyone a vegan? [Y/n]: ", end="")
user_input()
print("Is anyone a vegetarian? [Y/n]: ", end="")
user_input()
print("Is anyone on a gluten-free diet? [Y/n]: ", end="")
user_input()

print(restaurant_criteria)

restaurant_choices = restaurants
for restaurant in restaurants:
    print("current:", restaurant)
    for i in range(1, 3):
        print("checking")
        if restaurant_criteria[i]:
            if not restaurant[i]:
                print(restaurant[0])
                restaurant_choices.remove(restaurant)

print("Restaurant choices:")
for restaurant in restaurant_choices:
    print(restaurant[0])
