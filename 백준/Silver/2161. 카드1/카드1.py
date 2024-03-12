n = int(input())
card = [i+1 for i in range(n)]
answer = []
while len(card) != 1 :
    answer.append(card.pop(0))
    card.append(card.pop(0))

for i in answer :
    print(i, end=' ')
print(card[0])