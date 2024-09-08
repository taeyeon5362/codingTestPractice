def solution(s):
    answer = [-1]
    for i in range(1, len(s)) :
        if s[i] in s[:i] :
                answer.append(i - s[0:i].rindex(s[i]))
        else :
            answer.append(-1)
    return answer