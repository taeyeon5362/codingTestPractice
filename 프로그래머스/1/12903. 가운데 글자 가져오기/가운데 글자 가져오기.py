def solution(s):
    answer = ''
    li = len(s) // 2
    if len(s) % 2 == 0 :
        return s[li-1:li+1]
    else :
        return s[li]