import sys
input = sys.stdin.readline

while True :
    try :
        n, k = map(int, input().split())
        total_chickens = n 

        while n >= k :
            new_chickens = n // k
            total_chickens += new_chickens
            n = new_chickens + (n % k)

        print(total_chickens)
    except :
        break