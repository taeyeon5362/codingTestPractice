def solution(numbers):
    numbers = list(map(str, numbers))
    answer = sorted(numbers, key=lambda x : x * 3, reverse=1)
    return str(int("".join(answer)))