def solution(my_str, n):
    i = 0
    answer = []
    for i in range(0,len(my_str),n) :
        answer.append(my_str[i:n+i])
    return answer