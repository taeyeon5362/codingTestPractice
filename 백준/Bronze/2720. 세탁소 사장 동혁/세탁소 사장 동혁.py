T = int(input())
change = [0, 0, 0, 0]

for _ in range(T) :
    c = int(input())
    change[0] = c // 25
    c = c % 25
    change[1] = c // 10
    c = c % 10
    change[2] = c // 5
    c = c % 5
    change[3] = c // 1
    print(change[0], change[1], change[2], change[3])