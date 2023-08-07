def solution(numbers, direction):
    answer = []
    if 'right' in direction :
        answer.append(numbers[-1])
        answer += numbers[0:-1:]
    else :
        answer = numbers[1::]
        answer.append(numbers[0])
    return answer