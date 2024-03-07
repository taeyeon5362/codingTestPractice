num_list = list(map(int, input().split()))
num = 0
for i in num_list :
    num += i * i
print(num % 10)