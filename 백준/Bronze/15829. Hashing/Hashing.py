L = int(input())
str = input()
r, m = 31, 1234567891
alphabet = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6,
            'g': 7, 'h': 8, 'i': 9, 'j': 10, 'k': 11, 'l': 12,
            'm': 13, 'n': 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18,
            's': 19, 't': 20, 'u': 21, 'v': 22, 'w': 23, 'x': 24,
            'y': 25, 'z': 26}
answer = 0
for i in range(L) :
    answer += (alphabet[str[i]] * (r ** i)) % m
    
print(answer%m)