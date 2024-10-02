y, m, d = map(int, input().split('-'))
n = int(input())
result = 0
for _ in range(n) :
     g_y, g_m, g_d = map(int, input().split('-'))
     if y < g_y :
          result += 1
     elif y == g_y :
          if m < g_m :
                result += 1
          elif m == g_m :
                if d <= g_d :
                    result += 1
                    

print(result)