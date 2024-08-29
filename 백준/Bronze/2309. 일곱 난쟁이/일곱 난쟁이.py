import sys
input = sys.stdin.readline

nan = []
for _ in range(9):
    n = int(input())
    nan.append(n)

sum_ = sum(nan)

for i in range(8):
    for j in range(i+1, 9):
        if sum_ - nan[i] - nan[j] == 100:
            fake1, fake2 = nan[i], nan[j]
            nan.remove(fake1)
            nan.remove(fake2)
            break
    if len(nan) == 7:
        break

nan.sort()
for height in nan:
    print(height)