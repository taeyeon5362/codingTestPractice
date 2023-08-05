def solution(num, k):
    arr = str(num)
    for i, v in enumerate(arr) :
        if int(v) == k :
            return i + 1
    return -1