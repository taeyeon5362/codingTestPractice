import sys
input = sys.stdin.readline

n = int(input())
answer = 0
location = []

for _ in range(n) :
    cow_num, loca = map(int, input().split())
    
    if len(location) == 0 :
        location.append([cow_num, loca])
        
    else :
        for i in location :
            if i[0] == cow_num :
                if i[1] != loca :
                    answer += 1
                    i[1] = loca
                    break
                elif i[1] == loca :
                    break
            else :
                continue
        else :
            location.append([cow_num, loca])            
print(answer)
                
            