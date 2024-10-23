import sys
input = sys.stdin.readline

A, B = map(int, input().split())
data = [0]
sum = 0

for i in range(1, B+1):
    for j in range(i):
        data.append(i)

for i in range(A, B+1):
    sum += data[i]
    
print(sum)