def solution(n):
    arr = list(str(n))
    answer = 0
    for i in arr :
        answer += int(i)
    return answer