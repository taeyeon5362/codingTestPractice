def solution(myString):
    answer = ''
    arr = myString.lower()
    for i in arr :
        if i == 'a' :
            answer += 'A'
        else :
            answer += i
    return answer