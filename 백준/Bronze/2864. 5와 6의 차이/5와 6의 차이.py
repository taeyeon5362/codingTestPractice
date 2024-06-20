import sys
input = sys.stdin.readline

a, b = input().split()
c = a.replace('5','6')
d = b.replace('5','6')

e = a.replace('6','5')
f = b.replace('6','5')

print(int(e) + int(f), int(c) + int(d))