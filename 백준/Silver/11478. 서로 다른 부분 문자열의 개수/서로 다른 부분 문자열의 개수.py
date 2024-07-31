s = input()
list = set()
for i in range(len(s)) :
    for j in range(i,len(s)) :
        list.add(s[i:j+1])

print(len(list))