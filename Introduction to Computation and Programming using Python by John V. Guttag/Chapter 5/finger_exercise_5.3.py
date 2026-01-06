"""Finger exercise: Write a list comprehension that 
generates all non-primes between 2 and 100."""

my_list = [x for x in range(2,100) if not [z for z in range(2,int(x**0.5 +1)) if x%z == 0]]
print(my_list)