def solution(num_list):
    answer = 0
    for j in num_list :
        while(1) :
            if j > 1 :
                answer += 1
                j = j // 2
            else :
                break
    return answer