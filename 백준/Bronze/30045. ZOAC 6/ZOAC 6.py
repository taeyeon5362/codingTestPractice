import sys
input = sys.stdin.readline

n = int(input())
answer = 0

for _ in range(n) :
    s = input()
    if '01' in s or 'OI' in s :
        answer += 1

print(answer)