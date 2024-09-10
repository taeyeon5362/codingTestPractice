import sys
input = sys.stdin.readline

n, x = map(int, input().split())
a = list(map(int, input().split()))
answer = []

for i in range(n-1) :
    answer.append(a[i]*x + a[i+1]*x)

print(min(answer))