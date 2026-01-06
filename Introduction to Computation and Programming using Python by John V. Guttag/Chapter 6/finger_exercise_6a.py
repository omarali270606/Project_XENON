# Fibonacci numbers (he used female rabbits as an example)

def females(n,a=1,b=0):
    if n == 0:
        return a
    else:
        return females(n-1,a=a+b,b=a)
