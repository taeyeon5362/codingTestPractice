import sys
input = sys.stdin.readline

l ,p = map(int, input().split())
o, t, th, f, fi = map(int, input().split())
lp = l * p
print(o-lp, t-lp, th-lp, f-lp, fi-lp)