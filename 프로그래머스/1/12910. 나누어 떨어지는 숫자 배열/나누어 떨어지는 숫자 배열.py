def solution(arr, divisor):
    answer = []
    err = -1
    for i in arr :
        if i % divisor == 0 :
            answer.append(i)
    answer.sort()
    if not answer :
        answer.append(err)
    return answer