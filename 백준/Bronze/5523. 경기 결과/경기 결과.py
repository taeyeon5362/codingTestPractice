from sys import stdin

a_win = 0
b_win = 0
for _ in range(int(stdin.readline())):
    a, b = map(int, stdin.readline().split())
    if a > b:
        a_win += 1
    elif a < b:
        b_win += 1
print(a_win, b_win)