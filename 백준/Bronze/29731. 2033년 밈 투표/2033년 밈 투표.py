import sys
input = sys.stdin.readline

N = int(input())
rick = ['Never gonna give you up',
        'Never gonna let you down',
        'Never gonna run around and desert you',
        'Never gonna make you cry',
        'Never gonna say goodbye',
        'Never gonna tell a lie and hurt you',
        'Never gonna stop']
answer = 0

for i in range(N) :
    hac = input().rstrip()
    if hac in rick :
        answer += 1

if answer == N :
    print('No')
else :
    print('Yes')