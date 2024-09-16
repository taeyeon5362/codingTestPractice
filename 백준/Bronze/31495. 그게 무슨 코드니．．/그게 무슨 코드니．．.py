str = input()
if str[0] == str[-1] == '"' and len(str[1:-1]) > 0:
        print(str[1:-1])
else :
        print('CE') 