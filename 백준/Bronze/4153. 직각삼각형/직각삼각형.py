while(1) :
    a, b, c = map(int, input().split())
    if a == 0 and b == 0 and c == 0 :
        break
    else :
        if a*a + b*b == c*c :
            print('right')
        elif a*a + c*c == b*b :
            print('right')
        elif b*b + c*c == a*a :
            print('right')    
        else :
            print('wrong')