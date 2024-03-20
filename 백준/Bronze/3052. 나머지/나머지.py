answer = []
for i in range(10) :
    a = int(input())
    answer.append(a%42)

result = list(set(answer))
print(len(result))