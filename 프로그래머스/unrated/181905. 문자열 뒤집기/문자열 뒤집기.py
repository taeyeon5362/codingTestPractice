def solution(my_string, s, e):
    answer1 = my_string[s:e+1]
    answer2 = answer1[::-1]
    arr = my_string[:s] + answer2 + my_string[e+1::]
    return arr