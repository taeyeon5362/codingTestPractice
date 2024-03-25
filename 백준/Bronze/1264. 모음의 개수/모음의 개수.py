answer = 0
while True :
    a = input().lower()
    if a == '#' :
        break
    else :
        for i in a :
            if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u' :
                answer += 1
        print(answer)
        answer = 0

