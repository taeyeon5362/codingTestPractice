import sys
input = sys.stdin.readline

n = int(input().rstrip())
s = input().rstrip()

two = 0
e = 0

for i in s :
    if i == '2' :
        two += 1
    elif i == 'e' :
        e += 1

if two > e :
    print(2)
elif e > two :
    print('e')
else :
    print('yee')