n = int(input())
l = 1

while n > l:
    n -= l
    l += 1

#짝수
if l % 2 == 0:
    a = n
    b = l - n + 1
#홀수
elif l % 2 == 1:
    a = l - n + 1
    b = n

print(f'{a}/{b}')