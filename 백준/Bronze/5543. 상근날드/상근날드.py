import sys
input = sys.stdin.readline

menu = [int(input()) for _ in range(5)]
set_menu = [] 

for i in range(3) :
        set_menu.append(menu[i] + menu[3])
        set_menu.append(menu[i] + menu[4])

set_menu.sort()

print(set_menu[0]-50)