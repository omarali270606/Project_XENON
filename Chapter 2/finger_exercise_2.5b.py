highest_odd = None
i = 0
for i in range(10):
    number = int(input('Please enter an integer: '))
    if number%2 != 0:
        highest_odd = number if highest_odd is None or number > highest_odd else highest_odd
if highest_odd is not None:
    print(highest_odd)
else:
    print('no odd numbers')