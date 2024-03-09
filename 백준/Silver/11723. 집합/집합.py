import sys
input = sys.stdin.readline

T = int(input())
s = set()

for _ in range(T) :
    com = input().split()
    if len(com) == 1 :
        a = com[0]
    else :
        a, x = com

    if a == 'add' :
        s.add(int(x))
    elif a == 'remove' :
        if int(x) in s : 
            s.remove(int(x))
    elif a == 'check' :
        if int(x) in s :
            print(1)
        else :
            print(0)
    elif a == 'toggle' :
        if int(x) in s :
            s.remove(int(x))
        else :
            s.add(int(x))
    elif a == 'all' :
        s = {1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20}
    else :
        s.clear()