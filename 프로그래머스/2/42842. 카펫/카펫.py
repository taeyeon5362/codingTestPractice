def solution(brown, yellow):
    answer = []
    total = brown + yellow
    for i in range(1, total + 1) :
        if(total / i) % 1 == 0 :
            a = total / i
            if a >= i :
                if 2 * a + 2 * i == brown + 4 :
                    return [a, i]
    return answer