# global variable & local variable
# local variable cant access from another function

calculation_to_hours = 24
name_of_unit = "hours"

def days_to_units(num_of_days, custom_message="Good"):
    print(f"{num_of_days} days are {num_of_days * calculation_to_hours} {name_of_unit}")

user_input = input("Hey user, enter a number of days and I will convert it to hours!\n")
print(user_input)