def solution(t, p):
    answer = 0

    for i in range(len(t)) :
        str = t[i:i+len(p)]
        if len(str) == len(p) :
            if int(str) <= int(p) :
                answer += 1
            
    return answer