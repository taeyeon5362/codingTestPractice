import sys
input = sys.stdin.readline

n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

ab = a+b
ab.sort()

for i in ab :
     print(i, end=' ')