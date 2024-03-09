n = int(input())
answer = 0

for i in range(1, n+1) :
    if i < 100 :
        answer += 1
    elif i >= 100 :
        a = int(str(i)[0]) - int(str(i)[1])
        b = int(str(i)[1]) - int(str(i)[2])
        if a == b :
            answer += 1
print(answer)