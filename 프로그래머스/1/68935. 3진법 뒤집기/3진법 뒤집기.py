def solution(n):
    answer = ''
    while (n > 0) :
        r = n % 3
        n = n // 3
        answer += str(r)

    return int(answer, 3)