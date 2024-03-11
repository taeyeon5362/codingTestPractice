num_list1 = set(range(1,10001))
num_list2 = set()
    
for i in range(1, 100001) :
    for j in str(i) :
        i += int(j)
    num_list2.add(i)

self_num = sorted(num_list1 - num_list2)
for i in self_num :
    print(i)