import sys
input = sys.stdin.readline

n = int(input())
x = list(map(int, input().split()))

sortArr = list(sorted(set(x)))
dic = {}

for i, v in enumerate(sortArr):
    dic[v] = i

for i in x:
    print(dic[i], end=' ')