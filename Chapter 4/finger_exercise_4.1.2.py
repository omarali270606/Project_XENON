# Finger exercise: Write a function mult that accepts either one or
# two ints as arguments. If called with two arguments, the function
# prints the product of the two arguments. If called with one argument,
# it prints that argument.

def mult(x, y = None):
    if y != None:
        print(y*x)
    else:
        print(x)