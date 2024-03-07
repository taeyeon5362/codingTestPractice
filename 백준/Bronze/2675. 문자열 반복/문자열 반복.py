T = int(input())
for _ in range(T):
    a, b = input().split()
    a = int(a)
    for i in b :
        print(i*int(a), end='')
    print()