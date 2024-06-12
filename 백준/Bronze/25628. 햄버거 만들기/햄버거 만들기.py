a, b = map(int, input().split())
result = 0
while True :
    if a <= 1 :
        break
    if b <= 0 :
        break
    a -= 2
    b -= 1
    result += 1

print(result)
