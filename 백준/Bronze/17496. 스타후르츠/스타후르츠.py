n, t, c, p =  map(int, input().split())
answer = 0
for i in range(t+1, n+1, t) :
    answer += c * p
print(answer)