import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    zeroone = []
    n = int(input())
    while n > 0:
        zeroone.append(n%2)
        n = n//2

    for i, v in enumerate(zeroone) :
        if v == 1 :
            print(i, end=' ')
            
    