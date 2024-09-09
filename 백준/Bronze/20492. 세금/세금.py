import sys
input = sys.stdin.readline

n = int(input())

print(int(n*0.78), int((n-n*0.8)*0.78) + int(n*0.8))