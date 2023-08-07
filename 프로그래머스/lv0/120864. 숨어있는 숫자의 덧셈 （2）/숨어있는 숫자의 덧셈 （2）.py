import re
def solution(my_string):
    answer = 0
    arr1 = str(re.sub(r"[^0-9]", " ", my_string))
    arr2 = arr1.split()
    for i in arr2 :
        answer += int(i)
    return answer
