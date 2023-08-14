def solution(array, n):
    MAX = 101
    answer = 0
    array.sort()
    for i in array :
        if abs(n - i) < MAX :
            MAX = abs(n - i)
            answer = i
    return answer


