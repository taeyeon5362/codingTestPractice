import sys
input = sys.stdin.readline

x, y = input().split()
x = x[::-1]
y = y[::-1]
xy = int(x) + int(y)

print(int(str(xy)[::-1]))