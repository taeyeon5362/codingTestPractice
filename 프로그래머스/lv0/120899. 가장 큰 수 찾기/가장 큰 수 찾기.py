def solution(array):
    answer = [0,0]
    answer[0] += max(array)
    answer[1] += array.index(max(array))
    return answer