n, k = map(int, input().split())
list = list(map(int,input().split()))

tem = []
tem.append(sum(list[:k]))

for i in range(n-k) :
    tem.append(tem[i] - list[i] + list[k+i])
print(max(tem))