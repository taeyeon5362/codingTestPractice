def solution(a, d, included):
    answer = 0
    for i in range(len(included)) :
        if included[i] == True :
            answer += i * d + a
    return answer