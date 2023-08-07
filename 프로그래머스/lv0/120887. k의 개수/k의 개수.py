def solution(i, j, k):
    arr = ''
    k = str(k)
    cnt = 0
    for l in range(i,j+1) :
        arr += str(l)
    for m in arr :
        if m == k :
            cnt += 1
            
    return cnt