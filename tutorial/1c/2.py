restaurants = [
    ["Corner Café", True, True, True],
    ["Main Street Pizza Company", True, False, True],
    ["The Chef’s Kitchen", True, True, True],
    ["Joe’s Gourmet Burgers", False, False, False],
    ["Mama’s Fine Italian", True, False, False],
]
restaurant_criteria = [False]


def user_input(personal_requirement):
    print(f"Is anyone {personal_requirement}? [Y/n]: ", end="")
    response = None
    while not (response == (True or False)):
        response = input()
        if response == None:
            response = True
        else:
            if response.lower() == ("y" or "yes"):
                response = True
            elif response.lower() == ("n" or "no"):
                response = False
            else:
                print("please enter a valid answer: ", end="")
    restaurant_criteria.append(response)


user_input("a vegan")
user_input("a vegetarian")
user_input("on a gluten-free diet")

print(restaurant_criteria)

restaurant_choices = restaurants
items_to_be_removed_becuase_python_is_a_bitch = []
for restaurant in restaurants:
    for i in range(1, 4):
        if restaurant_criteria[i]:
            if not restaurant[i]:
                # for some reason modifing the list here messes up the loop, so i'm modifying outside of the loop
                items_to_be_removed_becuase_python_is_a_bitch.append(restaurant)

for item in items_to_be_removed_becuase_python_is_a_bitch:
    if item in restaurant_choices:
        restaurant_choices.remove(item)

print("\nRestaurant choices:")
for restaurant in restaurant_choices:
    print(restaurant[0])
