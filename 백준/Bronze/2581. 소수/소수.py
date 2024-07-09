n = int(input())
m = int(input())
answer = []
for i in range(n, m+1) :
    sosu = 0
    if i > 1 :
        for j in range(2, i) :
            if i % j == 0 :
                sosu += 1
        if sosu == 0 :
            answer.append(i)
if len(answer) == 0 :
    print(-1)
else :
    print(sum(answer))
    print(min(answer))