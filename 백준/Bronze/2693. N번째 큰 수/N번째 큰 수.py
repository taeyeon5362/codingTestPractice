T = int(input())
for _ in range(T) :
    score = list(map(int, input().split()))
    score.sort()
    print(score[-3])