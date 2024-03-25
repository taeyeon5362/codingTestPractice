num = int(input())
li = []
for _ in range(num) :
    a = int(input())
    li.append(a)
li.sort()
for i in li :
    print(i)