import sys
input = sys.stdin.readline

T = int(input())
s = []
for _ in range(T) :
    com = input().split()
    if len(com) == 1 :
        a = com[0]
    else :
        a, x = com

    if a == 'push' :
        s.append(int(x))
    elif a == 'pop' :
        if len(s) != 0 :
            top = s.pop()
            print(top)
        else :
            print(-1)
    elif a == 'size' :
        print(len(s))
    elif a == 'empty' :
        if len(s) != 0 :
            print(0)
        else :
            print(1)
    else :
        if len(s) != 0 :
            print(s[-1])
        else :
            print(-1)