# Finger exercise: Write a program that prints the sum of the prime
# numbers greater than 2 and less than 1000. Hint: you probably want
# to use a for loop that is a primality test nested inside a for loop that
# iterates over the odd integers between 3 and 999.

sum = 2
for i in range(3,1000,2):
    is_prime = True
    for k in range (3,int(i**0.5)+1,2):
        if i%k == 0:
            is_prime = False
            break
    if is_prime:
        sum += i
print(sum)