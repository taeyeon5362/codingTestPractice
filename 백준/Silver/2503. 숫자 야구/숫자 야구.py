from itertools import permutations

n = int(input())
num = list(permutations([1,2,3,4,5,6,7,8,9], 3))

for i in range(n) :
    ask, strike, ball = map(int, input().split())
    ask = list(str(ask))
    remove_cnt = 0

    for j in range(len(num)) :
        strike_cnt = ball_cnt = 0
        j -= remove_cnt

        for k in range(3) :
            if int(ask[k]) in num[j] :
                if k == num[j].index(int(ask[k])) :
                    strike_cnt += 1
                else :
                    ball_cnt += 1
        if strike_cnt != strike or ball_cnt != ball :
            num.remove(num[j])
            remove_cnt += 1

print(len(num))