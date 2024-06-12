a = list(map(int, input().split()))
c = [1, 1, 2, 2, 2, 8] #킹 1개, 퀸 1개, 룩 2개, 비숍 2개, 나이트 2개, 폰 8개
li = [0, 0, 0, 0, 0, 0]

for i in range(len(a)) :
    if a[i] == c[i] :
        continue
    else :
        li[i] = c[i] - a[i]
print(*li)