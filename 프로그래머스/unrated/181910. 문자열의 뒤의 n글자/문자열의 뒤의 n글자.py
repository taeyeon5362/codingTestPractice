def solution(my_string, n):
    answer = my_string[::-1]
    answer = answer[:n:]
    return answer[::-1]