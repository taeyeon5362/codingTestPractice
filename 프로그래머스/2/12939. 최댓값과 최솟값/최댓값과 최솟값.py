def solution(s):
    inte = []
    answer = ''
    s = s.split(' ')
    for i in s :
        inte.append(int(i))
    answer += str(min(inte)) + ' ' + str(max(inte))
    return answer