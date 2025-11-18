
temp = 5
is_raining = False
is_sunny = False
#  or operator
# if temp > 35 or temp < 10 or is_raining:
#     print("The outdoor event is cancelled.")
# else:
#     print("The outdoor event is still scheduled.")


if temp >= 35 and is_sunny:
    print("It is hot outside and it is sunny.")
elif temp <= 5 and not is_sunny:
    print("It is cold outside and it is cloudy")