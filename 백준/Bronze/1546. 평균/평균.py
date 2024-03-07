T = int(input())
num = list(map(int, input().split()))
max_num = max(num)
avg = 0

for i in num :
    avg += i / max_num * 100

print(avg/T)



