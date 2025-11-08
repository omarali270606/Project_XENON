def log(x, base, epsilon):
    ''' Assumes x and epsilon int or float, base an int,
x > 1, epsilon > 0 & power >= 1
Returns float y such that base**y is within epsilon
of x. '''  
    if base in [0,1]:
        return
    else:
        high = 1
        while base**high < x:
            high += 1
        low = high - 1
        power = (high+low) / 2
        while abs(x-base**power) > epsilon:
            if base**power < x:
                low = power
            else:
                high = power
            power = (high+low) / 2
        y = power
        return y
