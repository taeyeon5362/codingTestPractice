answer = []
people = 0
for i in range(4) :
    
    a, b = map(int, input().split())
    people = people - a + b
    answer.append(people)

print(max(answer))