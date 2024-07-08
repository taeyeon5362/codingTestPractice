while True :
    n = int(input())
    answer = []
    if n == -1 :
        break
    else :
        for i in range(1, n) :
            if n % i == 0 :
                answer.append(i)
        if sum(answer) == n :
            print(n, '= ', end='')
            for i in range(len(answer)) :
                if i == len(answer) - 1 :
                    print(answer[i], end='')
                else :
                    print(answer[i], '+ ', end='')
            print()
        else :
            print(n, 'is NOT perfect.')