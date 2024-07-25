import sys
input = sys.stdin.readline

n, m = map(int, input().split())

s_set = set()
for _ in range(n):
    s_set.add(input().rstrip())

result = 0
for _ in range(m):
    s = input().rstrip()
    if s in s_set:
        result += 1

print(result)