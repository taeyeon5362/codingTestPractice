a, b = map(int, input().split())
c = (str(a//b) + ".")
a = (a % b) * 10

for i in range(1000):
    c += str(a//b)
    a = (a % b)*10
print(c)