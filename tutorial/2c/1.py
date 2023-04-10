import requests


# option 1: manually input data
# temperature_in_fahrenheit = []
# for i in range(10):
#     temperature_in_fahrenheit.append(int(input("Input temperature:")))

# option 2: fake data
# temperature_in_fahrenheit = [98, 100, 121, 105, 119, 107, 97, 92, 99, 102]

# option 3: api
# get bored so i learned this
api_url = "https://api.open-meteo.com/v1/forecast?latitude=3.14&longitude=101.69&hourly=temperature_2m&temperature_unit=fahrenheit"
response = requests.get(api_url)
temperature_in_fahrenheit = response.json()["hourly"]["temperature_2m"]


for i in temperature_in_fahrenheit[:10]:
    print(f"Fahrenheit: {i}")
    print(f"Celsius: {(i - 32) * 5 / 9}")

print("All temperatures processed")
