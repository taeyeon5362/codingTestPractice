def solution(num_list):
    answer1 = sum(num_list[0::2])
    answer2 = sum(num_list[1::2])
    if answer1 > answer2 :
        return answer1
    else :
        return answer2
    
    
        