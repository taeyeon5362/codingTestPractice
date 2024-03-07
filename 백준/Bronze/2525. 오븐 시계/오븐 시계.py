h, m =  map(int, input().split())
p = int(input())

h += p // 60
m += p % 60

if m >= 60 :
    h += 1
    m -= 60
if h >= 24 :
    h -= 24
    
print(h, m)