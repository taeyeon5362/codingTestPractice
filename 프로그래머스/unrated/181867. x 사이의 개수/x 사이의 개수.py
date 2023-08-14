def solution(myString):
    myString = myString.split('x')
    answer = []
    for i in myString :
        answer.append(len(i))
    return answer