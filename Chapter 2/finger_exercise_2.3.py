x,y,z = 3,6,9
highest_odd = None
if x%2==1:
    highest_odd = x
if y%2==1:
    if highest_odd == None or y>highest_odd:
        highest_odd = y
if z%2==1:
    if highest_odd == None or z>highest_odd:
        highest_odd = z

if highest_odd != None:
    print(highest_odd)
else:
    lowest_even = x
    if y < lowest_even:
        lowest_even = y
    if z < lowest_even:
        lowest_even = z
    print(lowest_even)

