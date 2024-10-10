import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
de = deque([])

for _ in range(N):
    a = list(map(int,input().split()))
     
    if a[0] == 1:
        de.appendleft(a[1])
         
    elif a[0] == 2:
        de.append(a[1])
     
    elif a[0] == 3:
        if len(de) == 0:
            print(-1)
        else :
            print(de.popleft()) 
             
    elif a[0] == 4:
        if len(de) == 0:
            print(-1)
        else :
            print(de.pop())

    elif a[0] == 5:
        print(len(de))

    elif a[0] == 6 :
        if len(de) == 0:
            print(1)
        else:
            print(0)

    elif a[0] == 7:
        if len(de) == 0:
            print(-1)
        else:
            print(de[0])

    elif a[0] == 8 :
        if len(de) == 0:
            print(-1)
        else :
            print(de[-1])
