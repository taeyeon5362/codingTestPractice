import sys
input = sys.stdin.readline

n = int(input())
st = []
for _ in range(n) :
    
    x = list(map(int, input().split()))
    if len(x) == 2 :
        st.append(x[1])
    else :
        if x[0] == 2 :
            if len(st) == 0 :
                print(-1)
            else :
                print(st.pop())
        elif x[0] == 3 :
            print(len(st))
        elif x[0] == 4 :
            if len(st) == 0 :
                print(1)
            else :
                print(0)
        elif x[0] == 5 :
            if len(st) == 0 :
                print(-1)
            else :
                print(st[-1])
