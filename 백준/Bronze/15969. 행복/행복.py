import sys
input = sys.stdin.readline

N = int(input())
student = list(map(int, input().split()))
student.sort()
print(student[N-1] - student[0])