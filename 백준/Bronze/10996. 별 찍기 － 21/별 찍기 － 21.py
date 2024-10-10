N = int(input())

o = N//2

for i in range(N) :
    if N % 2 == 0 :
        print(('*' + ' ') * o)
        print((' ' + '*') * o)
    else :
        print(('*' + ' ') * o + '*')
        print((' ' + '*') * o)