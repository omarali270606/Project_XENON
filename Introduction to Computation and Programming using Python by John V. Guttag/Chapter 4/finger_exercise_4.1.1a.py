def find_root(x, power, epsilon):
    """Assumes x and epsilon int or float, power an int,
           epsilon > 0 & power >= 1
       Returns float y such that y**power is within epsilon of x.
           If such a float does not exist, it returns None."""
           
    # Find interval containing answer
    if x < 0 and power%2 == 0:
        return None #Negative number has no even-powered roots
        
    low = min(-1, x)
    high = max(1, x)
    
    # Use bisection search
    ans = (high + low)/2
    while abs(ans**power - x) >= epsilon:
        if ans**power < x:
            low = ans
        else:
            high = ans
        ans = (high + low)/2
    return ans

#
# --- YOUR CODE GOES HERE ---
#
# Your "finger exercise" is to *call* this function
# three times and print the sum.
#

print(find_root(25,2,0.001)+find_root(-8,3,0.001)+find_root(16,4,0.001))