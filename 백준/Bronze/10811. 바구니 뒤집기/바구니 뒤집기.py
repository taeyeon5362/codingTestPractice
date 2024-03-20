n, m = map(int, input().split())
basket = [i for i in range(1, n+1)]

for _ in range(m) :
    i, j = map(int, input().split())
    blank = basket[i-1:j]
    basket[i-1:j] = blank[::-1]
    
for i in range(n) :
    print(basket[i], end=' ')