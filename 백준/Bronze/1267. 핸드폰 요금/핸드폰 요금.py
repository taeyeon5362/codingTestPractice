T = int(input())
m = 0
y = 0
cash = list(map(int, input().split()))
for i in cash:
    m += (i // 60 + 1) * 15
    y += (i // 30 + 1) * 10
if m > y:
    print('Y', y)
elif y > m:
    print('M', m)
elif y == m:
    print('Y M', m)
