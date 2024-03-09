C = int(input())

for _ in range(C) :
    a = list(map(int, input().split()))
    avg = sum(a[1:]) / a[0]
    avg_plus = 0
    for i in a[1:] :
        if i > avg :
            avg_plus += 1
    percentile = avg_plus/a[0] * 100
    print('{0:0.3f}%'.format(percentile))
        