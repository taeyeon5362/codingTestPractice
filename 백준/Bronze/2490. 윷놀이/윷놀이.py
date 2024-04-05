answer = []
for _ in range(3) :
    a = list(map(int, input().split()))
    cnt_0 = a.count(0)
    if cnt_0 == 1 :
        answer.append('A')
    elif cnt_0 == 2 :
        answer.append('B')
    elif cnt_0 == 3 :
        answer.append('C')
    elif cnt_0 == 4 :
        answer.append('D')
    else :
        answer.append('E')
for i in answer :
    print(i)