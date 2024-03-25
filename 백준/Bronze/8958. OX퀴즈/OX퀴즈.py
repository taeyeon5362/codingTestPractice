a = int(input())
for _ in range(a) :
    b = list(input())
    score = 0
    plus = 0
    for i in b :
        if i == 'O' :
            plus += 1
            score = score + plus
        elif i == 'X' :
            plus = 0
    print(score)