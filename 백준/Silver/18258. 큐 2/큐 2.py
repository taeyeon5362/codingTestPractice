import sys
input = sys.stdin.readline
from collections import deque

N = int(input())
que = deque([])

for _ in range(N):
    a = list(input().split())
    if a[0] == 'push':
        que.insert(0, a[1])
         
    elif a[0] == 'pop':
        if len(que) == 0:
            print(-1)
        else :
            print(que.pop())
             
    elif a[0] == 'size':
        print(len(que))
         
    elif a[0] == 'empty' :
        if len(que) == 0:
            print(1)
        else:
            print(0)
             
    elif a[0] == 'front':
        if len(que) == 0:
            print(-1)
        else:
            print(que[-1])
             
    elif a[0] == 'back' :
        if len(que) == 0:
            print(-1)
        else :
            print(que[0])