def solution(numbers):
    answer = sorted(numbers)
    if answer[0] * answer[1] > answer[-1] * answer[-2] :
        return answer[0] * answer[1]
    else :
        return answer[-1] * answer[-2]