t = int(input())
answer = []
for _ in range(t) :
    a = list(map(int, input().split()))
    if a[0] == a[1] == a[2] :
        answer.append(a[0]*1000 + 10000)
    elif a[0] == a[1] or a[0] == a[2]:
        answer.append(a[0]*100 + 1000)
    elif a[1] == a[2] :
        answer.append(a[1]*100 + 1000)
    else :
        a.sort()
        answer.append(a[2] * 100)
answer.sort()
print(answer[-1])