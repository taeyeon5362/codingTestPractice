t = int(input())
cnt = []
for _ in range(t) :
    a = int(input())
    cnt.append(a)
zero = cnt.count(0)
one = cnt.count(1)
if zero > one :
    print('Junhee is not cute!')
else :
    print('Junhee is cute!')