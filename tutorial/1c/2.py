restaurants = {
    "Corner Café": [True, True, True],
    "Main Street Pizza Company": [True, False, True],
    "The Chef’s Kitchen": [True, True, True],
    "Joe’s Gourmet Burgers": [False, False, False],
    "Mama’s Fine Italian": [True, False, False],
}
restaurant_criteria = []


def user_input(personal_requirement):
    print(f"Is anyone {personal_requirement}? [Y/n]: ", end="")
    response = None
    while response is None:
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
user_input("a gluten-free guy")

print(restaurant_criteria)
restaurant_choices = restaurants.copy()

for restaurant, criteria in restaurants.items():
    for i, meets_criteria in enumerate(criteria):
        if restaurant_criteria[i] and not meets_criteria:
            if restaurant in restaurant_choices:
                del restaurant_choices[restaurant]
                break

print("\nRestaurant choices:")
for restaurant in restaurant_choices:
    print(restaurant)
