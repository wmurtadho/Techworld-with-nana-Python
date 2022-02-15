# return digunakan ketika mau assigned to new variable
# user type() to find type data 

calculation_to_hours = 24
name_of_unit = "hours"

def days_to_units(num_of_days):
    if num_of_days > 0:
        return f"{num_of_days} days are {num_of_days * calculation_to_hours} {name_of_unit}"
    elif num_of_days == 0:
        return "you entered a 0, please enter a valid positive number"

def validate_and_execute():
    if user_input.isdigit():
        user_input_number = int(user_input)
        calculated_value = days_to_units(user_input_number)
        print(calculated_value)
    else:
        print("your input is not a number. Don't ruin my program!")

user_input = input("Hey user, enter a number of days and I will convert it to hours!\n")
validate_and_execute()
