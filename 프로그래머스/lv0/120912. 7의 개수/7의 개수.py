def solution(array):
    answer = ''
    cnt = 0
    for i in array :
        answer += str(i)
    for i in answer :
        if i == '7': 
            cnt += 1
    return cnt