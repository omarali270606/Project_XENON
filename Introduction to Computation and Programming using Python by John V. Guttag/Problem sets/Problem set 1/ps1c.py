## 6.100A PSet 1: Part C
## Name:
## Time Spent:
## Collaborators:

##############################################
## Get user input for initial_deposit below ##
##############################################
initial_deposit = float(input('Enter the initial deposit: '))

#########################################################################
## Initialize other variables you need (if any) for your program below ##
#########################################################################
house_cost = 800000
down_payment = 0.25 * house_cost
months = 36
epsilon = 100
high = 1
low = 0
amount_saved = 0
r = 0
steps = 0

##################################################################################################
## Determine the lowest rate of return needed to get the down payment for your dream home below ##
##################################################################################################
if initial_deposit * ((1+1/12)**months) < down_payment:
        r = None

if r != None:
    while abs(down_payment - amount_saved) > epsilon:
        steps += 1
        if initial_deposit * ((1+1/12)**months) < down_payment:
            r = None
            break
        guess = (high + low) / 2
        amount_saved = initial_deposit* ((1+guess/12)**months)
        if amount_saved < down_payment:
            low = guess
        if amount_saved > down_payment:
            high = guess
    r = guess

print('Best savings rate:' ,r)
print('Steps in bisection search:', steps)