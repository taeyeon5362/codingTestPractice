import sys
input = sys.stdin.readline

T = int(input())
list = list(map(int, input().split()))
result = 0

list.sort()
dp = [0] * (T + 1)

for i in range(1, T):
    dp[i] = dp[i - 1] + (list[i] - list[i - 1]) * i
    result += dp[i]
print(result * 2)