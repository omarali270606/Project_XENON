'''
Finger exercise: Write a program that 
prints the sum of the prime numbers 
greater than 2 and less than 1000. 
'''
sum = 0
for number in range(3,1000,2):
    for check in range (3, int(number**0.5)+1,2):
        if number%check == 0:
            break
    else:
        sum += number
print(sum)