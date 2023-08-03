def solution(my_string, index_list):
    answer = ''
    for i in index_list :
        for index, value in enumerate(my_string) :
            if index == i :
                answer += value
    return answer