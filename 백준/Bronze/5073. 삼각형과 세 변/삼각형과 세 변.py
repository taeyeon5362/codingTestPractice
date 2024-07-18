import sys
input = sys.stdin.readline

while True:
    tr = sorted(list(map(int, input().strip().split())))
    if tr[0] == tr[1] == tr[2] == 0:
        break

    if tr[0] + tr[1] <= tr[2]:
        print("Invalid")
    else:
        tr_set = set(tr)
        if len(tr_set) == 1:
            print("Equilateral")
        elif len(tr_set) == 2:
            print("Isosceles")
        else:
            print("Scalene")