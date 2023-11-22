def solution(arr):
    i = min(arr)
    err = -1
    arr.remove(i)
    if not arr :
        arr.append(err)
    return arr