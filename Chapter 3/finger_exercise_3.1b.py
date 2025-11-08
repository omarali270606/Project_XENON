'''
Finger exercise: Write a program that 
asks the user to enter an integer 
and prints two integers, root and pwr, 
such that 1 < pwr < 6 and 
root**pwr is equal to the integer entered by the user. 
If no such pair of integers exists, 
it should print a message to that effect.
'''

integer = int(input('enter an integer: '))
found_root = False
if integer < 0:
    print('not found')
else:
    for root in range (int(integer**0.5) + 2):
        if root**2 > integer:
            break
        for pwr in range(2,6):
            if root**pwr == integer:
                found_root = True
                break
        if found_root:
            break
            
    if found_root:
        print(f'{root} power {pwr} is {integer}')
    else:
        print('not found')
