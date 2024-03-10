n, k = map(int, input().split())
coin_list = []
for i in range(n) :
    coin_list.append(int(input()))
coin_list.sort(reverse=True)
coin = 0
for i in coin_list :
    if k >= i :
        coin += k // i
        k %= i
        if k <= 0 :
            break
print(coin)