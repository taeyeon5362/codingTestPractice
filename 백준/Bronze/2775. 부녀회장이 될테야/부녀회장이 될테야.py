T = int(input())
for _ in range(T) :
    k = int(input()) #층
    n = int(input()) #호

    f0 = [i for i in range(1, n+1)] # 0층
    for i in range(k) :
        for j in range(1, n) :
            f0[j] += f0[j-1]
    print(f0[-1])