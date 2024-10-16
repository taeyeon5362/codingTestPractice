import sys
input = sys.stdin.readline

ball = ['S', '0', '0', 'B']

str = input()
for i in str :
    if i == 'A' :
        ball[0], ball[1] = ball[1], ball[0]
    elif i == 'B' :
        ball[0], ball[2] = ball[2], ball[0]
    elif i == 'C' :
        ball[0], ball[3] = ball[3], ball[0]
    elif i == 'D' :
        ball[1], ball[2] = ball[2], ball[1]
    elif i == 'E' :
        ball[1], ball[3] = ball[3], ball[1]
    elif i == 'F' :
        ball[2], ball[3] = ball[3], ball[2]

for i in ball :
    if i == 'S' :
        print(ball.index(i) + 1)

for i in ball :
    if i == 'B' :
        print(ball.index(i) + 1)