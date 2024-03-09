import sys
input = sys.stdin.readline

def roun_d(num) :
    return int(num) + (1 if num - int(num) >= 0.5 else 0)
n = int(input())
rou = roun_d(n * 0.15)

if n == 0 :
    print(0)
else :
    lst = []
    for _ in range(n) :
        level = int(input())
        lst.append(level)
    lst.sort()
    
    avg = 0
    for i in range(rou, n-rou) :
        avg += lst[i]
    avg = avg/(n-2 * rou)
    print(roun_d(avg))