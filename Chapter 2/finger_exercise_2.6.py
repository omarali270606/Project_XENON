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