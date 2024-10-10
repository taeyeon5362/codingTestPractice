N = int(input())
num = N*2-2

if N == 1 :
    print('*')

else :
    for i in range(1, N) :
        b = ((num * 2) + 1) - (i*4)
        s = ((num * 2) + 1) - ((i-1)*4)

        print(('*' + ' ')*(i-1) + '*'*s +(' '+'*')*(i-1))
        print(('*'+' ')*i + ' '*b + (' '+'*')*i)
     
    print(('*' + ' ')*num + '*')

    for i in range(N-1, 0, -1) :
        b = ((num * 2) + 1) - (i*4)
        s = ((num * 2) + 1) - ((i-1)*4)

        print(('*'+' ')*i + ' '*b + (' '+'*')*i)
        print(('*' + ' ')*(i-1) + '*'*s +(' '+'*')*(i-1))