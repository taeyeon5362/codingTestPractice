score = list(map(int, input().split()))
win = [100, 100, 200, 200, 300, 300, 400, 400, 500]

hacker = 0

for i in range(len(win)) :
    if score[i] > win[i] :
        hacker = 1
        break
        
if hacker :
    print("hacker")
else :
    if sum(score) < 100 :
        print("none")
    else :
        print("draw")