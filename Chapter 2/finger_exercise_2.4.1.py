# date = input("Enter your date in the form mm/dd/yyyy: ")
# year_of_birth = date[-4:]
# print(f"Your year of birth is {year_of_birth}.")

# 1. Get the input
date = input("Enter your date in the form mm/dd/yyyy: ")

# 2. Use the "True Clever" abstraction: split()
# This turns "10/26/2025" into a list: ['10', '26', '2025']
# This turns "5/7/98" into a list: ['5', '7', '98']
date_parts = date.split('/')
print(date_parts)
# 3. Get the last item from the list data structure.
# This is robust. It doesn't care how many characters are in the year.
year_of_birth = date_parts[-1]

# 4. Print the result
print(f"Your year of birth is {year_of_birth}.")
