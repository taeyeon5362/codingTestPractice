K = int(input())
li = []
for _ in range(K) :
    N = int(input())
    li.append(N)
    if N == 0 :
        li.pop()
        li.pop()
print(sum(li))
    