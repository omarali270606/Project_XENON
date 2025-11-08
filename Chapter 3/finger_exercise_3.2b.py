floors = 102
max_floors = 93
low = 0
high = floors
current_floor = (high+low)//2
used_eggs = 0
while high-low > 1:
    used_eggs += 1
    if current_floor > max_floors:
        high = current_floor
    else:
        low = current_floor
    current_floor = (low+high)//2
print(used_eggs)