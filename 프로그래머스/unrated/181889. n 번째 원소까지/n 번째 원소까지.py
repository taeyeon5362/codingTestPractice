def solution(num_list, n):
    answer = []
    for index, value in enumerate(num_list) :
        if index < n :
            answer.append(value)
    return answer