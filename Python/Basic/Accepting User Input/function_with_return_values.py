# return digunakan ketika mau assigned to new variable

calculation_to_hours = 24
name_of_unit = "hours"

def days_to_units(num_of_days):
    print(f"{num_of_days} days are {num_of_days * calculation_to_hours} {name_of_unit}")

user_input = input("Hey user, enter a number of days and I will convert it to hours!\n")
user_input_number = int(user_input)

calculated_value = days_to_units(user_input_number)
print(calculated_value)
