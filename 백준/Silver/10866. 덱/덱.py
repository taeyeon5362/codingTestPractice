import sys
input = sys.stdin.readline

N = int(input())
de = []

for _ in range(N):
    a = list(input().split())
    if a[0] == 'push_back':
        de.append(a[1])
    elif a[0] == 'push_front':
        de.insert(0, a[1])
    elif a[0] == 'pop_front':
        if len(de) == 0:
            print(-1)
        else :
            print(de.pop(0))         
    elif a[0] == 'pop_back':
        if len(de) == 0:
            print(-1)
        else :
            print(de.pop())
    elif a[0] == 'size':
        print(len(de))
    elif a[0] == 'empty' :
        if len(de) == 0:
            print(1)
        else:
            print(0)
    elif a[0] == 'front':
        if len(de) == 0:
            print(-1)
        else:
            print(de[0])
    elif a[0] == 'back' :
        if len(de) == 0:
            print(-1)
        else :
            print(de[-1])
               