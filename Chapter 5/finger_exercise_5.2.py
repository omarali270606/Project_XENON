"""
Finger exercise: Write an expression that 
evaluates to the mean of a tuple of numbers. 
Use the function sum.
"""

def mean(numbers):
    return sum(numbers)/len(numbers) if len(numbers) != 0 else None