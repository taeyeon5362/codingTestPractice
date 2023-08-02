def solution(s):
    answer = ''
    counter = {}
    for i in s :
        try : counter[i] += 1
        except : counter[i] = 1
    for key, value in counter.items():
        if value == 1 :
            answer += key
    return "".join(sorted(answer))