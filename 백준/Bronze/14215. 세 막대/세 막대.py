sq = sorted(list(map(int, input().split())))
if sq[0] + sq[1] > sq[2]:
    print(sum(sq))
else:
    print((sq[0] + sq[1]) * 2 - 1)