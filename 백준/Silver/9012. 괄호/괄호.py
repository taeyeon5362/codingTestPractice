T = int(input())
for _ in range(T) :
    a = input()
    stack = []
    for i in a :
        if i == '(' :
            stack.append(i)
        elif i == ')' :
            if stack:
                stack.pop()
            else: 
                print("NO")
                break
    else: 
        if not stack:
            print("YES")
        else:
            print("NO")