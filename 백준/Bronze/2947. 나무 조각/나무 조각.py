import sys
input = sys.stdin.readline

wood = list(map(int, input().split()))
for i in range(5):
    for j in range(4):
        if wood[j] > wood[j+1]:
            t = wood[j]
            wood[j] = wood[j+1]
            wood[j+1] = t
            print(*wood)