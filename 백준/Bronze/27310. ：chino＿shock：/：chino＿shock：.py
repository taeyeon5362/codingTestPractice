n = input()
under = 0

for i in n :
    if i == '_' :
        under += 1

print(len(n) + 2 + under*5)