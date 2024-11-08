import sys
input = sys.stdin.readline

n = int(input())
answer = 0
answer2 = 0 
for i in range(1, n+1) :
    answer += i
print(answer)
print(answer * answer)

for i in range(1, n+1) :
    answer2 += i * i * i
print(answer2)