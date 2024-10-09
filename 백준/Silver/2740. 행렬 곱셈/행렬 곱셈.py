import sys
input = sys.stdin.readline

a_list = []
b_list = []
ab_list = []

a_row, a_col = map(int, input().split())
for i in range(a_row) :
    a_num = list(map(int, input().split()))
    a_list.append(a_num)

b_row, b_col = map(int, input().split())
for i in range(b_row) :
    b_num = list(map(int, input().split()))
    b_list.append(b_num)

for i in range(a_row) :
    ab_list.append([])
    for j in range(b_col) :
        ab_list[i].append(0)

for i in range(a_row) :
    for j in range(b_col) :
        for k in range(a_col) :
            ab_list[i][j] += a_list[i][k] * b_list[k][j]

for i in range(a_row) :
    for j in range(b_col) :
        print(ab_list[i][j], end=' ')

    print()