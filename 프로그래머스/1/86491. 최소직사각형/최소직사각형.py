def solution(sizes):
    h = []
    w = []
    for i in sizes :
        if i[0] >= i[1] :
            h.append(i[0])
            w.append(i[1])
        else :
            w.append(i[0])
            h.append(i[1])
    h.sort(reverse=True)
    w.sort(reverse=True)
    return h[0] * w[0]