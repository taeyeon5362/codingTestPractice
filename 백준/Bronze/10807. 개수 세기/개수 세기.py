n = int(input())
num_list = list(map(int, input().split()))
v = int(input())
answer = 0

for i in num_list :
    if i == v :
        answer += 1
print(answer)