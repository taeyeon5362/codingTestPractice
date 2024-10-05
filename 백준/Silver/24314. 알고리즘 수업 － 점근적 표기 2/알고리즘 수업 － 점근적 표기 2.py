a1, a0 = map(int, input().split())
c = int(input())
N = int(input())

for i in range(N, 102):
    if a1 * i + a0 < c * i:
        print(0)
        break
else:
    print(1)