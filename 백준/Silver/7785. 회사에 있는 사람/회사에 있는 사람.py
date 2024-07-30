n = int(input())
dic = {}

for _ in range(n):
    name, enle = input().split()
    if enle == "enter":
        dic[name] = enle
    elif enle == "leave":
        if name in dic:
            dic.pop(name)
for name in sorted(dic.keys(), reverse=True):
    print(name)
