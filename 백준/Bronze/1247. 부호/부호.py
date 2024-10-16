for _ in range(3) :
    n = int(input())
    answer = 0
    for i in range(n) :
        s = int(input())
        answer += s

    if answer == 0 :
        print('0')
    elif answer >= 1 :
        print('+')
    else :
        print('-')