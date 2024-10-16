T = int(input())

for _ in range(T) :
    N = input()
    year = int(N[2:])

    if (int(N)+1) % year == 0 :
        print('Good')
    else :
        print('Bye')