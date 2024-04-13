x, y, w, h = map(int, input().split())
answer = []
answer.append(x)
answer.append(y)
answer.append(w-x)
answer.append(h-y)

answer.sort()

print(answer[0])