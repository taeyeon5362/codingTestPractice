import sys
input = sys.stdin.readline

a, b = map(int, input().split())
answer = 0

if a > b :
    answer = b * 2 + 1
elif a == b :
    answer = a + b - 1
else :
    answer = a * 2 - 1

print(answer)