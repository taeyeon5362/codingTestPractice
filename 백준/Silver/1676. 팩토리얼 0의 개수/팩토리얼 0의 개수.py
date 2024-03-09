n = int(input())
num = 1
for i in range(1, n+1) :
    num *= i
num = list(map(int, str(num)))
num = num[::-1]
cnt = 0
for i in num :
    if i != 0 :
        break
    elif i == 0 :
        cnt += 1
print(cnt)