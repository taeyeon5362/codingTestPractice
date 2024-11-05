import sys
input = sys.stdin.readline

N, D = map(int, input().split())

for _ in range(N) :
    str = ''
    s = input().rstrip()
    if D == 1 :
        for i in range(len(s)) :
            if s[i] == 'd' :
                str += 'q'
            elif s[i] == 'b' :
                str += 'p'
            elif s[i] == 'p' :
                str += 'b'
            elif s[i] == 'q' :
                str += 'd'
    if D == 2 :
        for i in range(len(s)) :
            if s[i] == 'd' :
                str += 'b'
            elif s[i] == 'b' :
                str += 'd'
            elif s[i] == 'p' :
                str += 'q'
            elif s[i] == 'q' :
                str += 'p'
    print(str)       