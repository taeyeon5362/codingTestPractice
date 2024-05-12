n = int(input())
s = input()
answer = 1
l = 0

for i in s :
    if i == 'S' :
        answer += 1
    else :
        if l == 0 :
            l += 1
        else :
            answer += 1
            l = 0
if answer >= n :
    print(n)
else :   
    print(answer)