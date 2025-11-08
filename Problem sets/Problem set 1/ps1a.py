yearly_salary = float(input('Enter your yearly salary: '))
portion_saved = float(input('Enter the percent of your salary to save, as a decimal: '))
cost_of_dream_home = float(input('Enter the cost of your dream home: '))

monthly = yearly_salary/12
portion_down_payment = cost_of_dream_home * 0.25
amount_saved = 0
months = 0

while amount_saved < portion_down_payment:
    annual_return = amount_saved * 0.05/12
    amount_saved += annual_return + monthly*portion_saved
    months += 1
print('Number of months:', months)