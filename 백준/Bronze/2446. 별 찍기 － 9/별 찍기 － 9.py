a = int(input())
for i in range(a, 0, -1):
    print(" " * (a - i) + "*" * (i * 2 - 1))
for i in range(1, a) :
    print(' ' * ((a - 1) - i) + '*' * (2 * i + 1))
