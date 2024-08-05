min = sum(list(map(int, input().split())))
man = sum(list(map(int, input().split())))
if min >= man :
    print(min)
else :
    print(man)