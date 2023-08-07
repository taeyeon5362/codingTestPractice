def solution(my_string):
    answer = ''
    arr = sorted(my_string.lower())
    for i in arr :
        answer += i
    return answer