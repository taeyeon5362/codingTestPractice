def solution(strArr):
    answer = []
    for index, value in enumerate(strArr) :
        if index % 2 == 0 :
            answer.append(value.lower())
        else :
            answer.append(value.upper())
    return answer
            