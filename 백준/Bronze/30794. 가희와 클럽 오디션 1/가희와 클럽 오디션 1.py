lv = input().split()
if lv[1] == 'miss' :
    print(0)
elif lv[1] == 'bad' :
    print(int(lv[0]) * 200)
elif lv[1] == 'cool' :
    print(int(lv[0]) * 400)
elif lv[1] == 'great' :
    print(int(lv[0]) * 600)
elif lv[1] == 'perfect' :
    print(int(lv[0]) * 1000)