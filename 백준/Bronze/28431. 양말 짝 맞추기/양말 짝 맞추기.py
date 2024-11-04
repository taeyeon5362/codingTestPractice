import sys
input = sys.stdin.readline

s = []
for i in range(5) :
    a = int(input())
    if a in s :
        s.remove(a)
    else :
        s.append(a)

print(s[0])