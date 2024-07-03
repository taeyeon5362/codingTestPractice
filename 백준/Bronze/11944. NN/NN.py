import sys
input = sys.stdin.readline

n, m = map(int, input().split())
answer = str(n) * n
print(answer[:m])