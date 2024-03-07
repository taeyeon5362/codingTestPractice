T = int(input())

for test_case in range(1, T + 1):
    b, c = map(int, input().split())
    print('Case #{}: {} + {} = {}'.format(test_case, b, c, b+c))