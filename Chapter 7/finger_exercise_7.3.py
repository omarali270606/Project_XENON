# Finger exercise: Write a program that first stores the first ten
# numbers in the Fibonnaci sequence to a file named fib_file. Each
# number should be on a separate line in the file. The program should
# then read the numbers from the file and print them.

with open('fib_file','w') as name_handle:
    a = 1
    b = 0
    for i in range(10):
        name_handle.write(str(a) + '\n')
        a,b = a+b,a

with open('fib_file', 'r') as name_handle:
    for line in name_handle:
        print(line.strip())