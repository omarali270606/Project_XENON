# Finger exercise: Write code that asks the user to enter their
# birthday in the form mm/dd/yyyy, and then prints a string of the
# form ‘You were born in the year yyyy.

date = input("Enter your date in the form mm/dd/yyyy: ")


date_parts = date.split('/')
print(date_parts)

year_of_birth = date_parts[-1]

print(f"Your year of birth is {year_of_birth}.")
