a, b = map(int, input().split())

a_list = set(map(int, input().split()))
b_list = set(map(int, input().split()))

a_b = a_list - b_list
b_a = b_list - a_list
print(len(a_b) + len(b_a))