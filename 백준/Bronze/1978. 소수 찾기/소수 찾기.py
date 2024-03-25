answer = 0
num = int(input())
li = list(map(int, input().split()))
for x in li :
    for i in range(2, x+1):
        if x % i == 0:
            if x == i :
                answer += 1
            break
print(answer)