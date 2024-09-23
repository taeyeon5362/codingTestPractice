import sys
input = sys.stdin.readline

s = input()
joi = 0
ioi = 0

for i in range(len(s)-3) :
        if s[i:i+3] == 'JOI' :
                joi += 1
        elif s[i:i+3] == 'IOI' :
                ioi += 1
        else :
                continue

print(joi)
print(ioi)