# Wind Chill (ºF) = 35.74 + 0.6215T - 35.75(V0.16) + 0.4275T(V0.16)

def get_wind_chill(temp, wind):
    far = (35.74 + (0.6215 * temp)) - (35.75 * (wind ** 0.16)) + (0.4275 * temp * (wind ** 0.16))
    return far


def cel_to_far(temp):
    far = (temp * 9.0 / 5.0) + 32
    return far


def show_stats(temp_input):
    for wind in range(1, 61):
        if wind % 5 == 0:
            temp = round(get_wind_chill(temp_input, wind), 2)
            print(f"At temperature {temp_input}F, and wind speed {wind} mph, the windchill is: {temp}F")


temp_input = float(input("What is the temperature? "))
temp_type = input("Fahrenheit or Celsius? (F or C): ").lower()

if temp_type == "f":
    show_stats(temp_input)

elif temp_type == "c":
    temp = cel_to_far(temp_input)
    show_stats(temp)

