import sys
input = sys.stdin.readline


n = int(input())
li = set(map(int, input().split()))
lis = list(li)
lis.sort()

for i in range(len(lis)) :
     print(lis[i], end=' ')