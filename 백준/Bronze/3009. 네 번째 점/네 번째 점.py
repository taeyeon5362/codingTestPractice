answer_a = []
answer_b = []
for _ in range(3) :
    a, b = map(int, input().split())
    if a in answer_a :
        answer_a.remove(a)
    else :
        answer_a.append(a)
    if b in answer_b :
        answer_b.remove(b)
    else :
        answer_b.append(b)
print(answer_a[0], answer_b[0])