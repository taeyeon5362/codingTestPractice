while True :
    list = input().split()
    if list[0] == '#' :
        break
    if int(list[1]) > 17 or int(list[2]) >= 80 :
        print(list[0], 'Senior')
    else :
        print(list[0], 'Junior')