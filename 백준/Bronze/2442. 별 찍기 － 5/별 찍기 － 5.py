a = int(input())
for i in range(a) :
    print(' ' * ((a - 1) - i), end = '')
    print('*' * (2 * i + 1))