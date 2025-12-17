# Finger exercise: The Empire State Building is 102 stories high. A
# man wanted to know the highest floor from which he could drop an
# egg without the egg breaking. He proposed to drop an egg from the
# top floor. If it broke, he would go down a floor, and try it again. He
# would do this until the egg did not break. At worst, this method
# requires 102 eggs. Implement a method that at worst uses seven
# eggs.


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