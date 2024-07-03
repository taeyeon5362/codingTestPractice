import math

L = int(input())
A = int(input())
B = int(input())
C = int(input())
D = int(input())

ko = math.ceil(A / C)
ma = math.ceil(B / D)
if ko >= ma :
    print(L - ko)
else :
    print(L - ma)