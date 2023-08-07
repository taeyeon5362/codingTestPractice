def solution(numbers, k):
    answer = (numbers * k)[::2]
    return answer[k-1]