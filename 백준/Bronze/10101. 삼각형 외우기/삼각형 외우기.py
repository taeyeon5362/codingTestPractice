import sys
input = sys.stdin.readline

tr = [int(input()) for i in range(3)]
if sum(tr) != 180 :
    print('Error')
else :
    tr = set(tr)
    if len(tr) == 1 :
        print('Equilateral')
    elif len(tr) == 2 :
        print('Isosceles')
    else :
        print('Scalene')
    