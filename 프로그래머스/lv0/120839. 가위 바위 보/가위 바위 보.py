def solution(rsp):
    answer = ''
    dic = {'2':'0', '5':'2', '0':'5'}
    for i in str(rsp):
        answer += dic[i]
    return answer