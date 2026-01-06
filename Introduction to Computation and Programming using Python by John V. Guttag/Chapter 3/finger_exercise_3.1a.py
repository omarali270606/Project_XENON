# Test if an int > 2 is prime. If not, print smallest divisor.
x = int(input('Enter number greater than 2: '))
greatest_divisor = None
for guess in range(int(x*(1/2)),1,-1):
    if x%guess == 0:
        greatest_divisor = guess
        break
if greatest_divisor != None:
    print(greatest_divisor)
else:
    print('prime')