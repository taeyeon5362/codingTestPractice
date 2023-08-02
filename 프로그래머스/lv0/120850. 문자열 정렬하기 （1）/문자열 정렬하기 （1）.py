import re
def solution(my_string):
    answer = re.sub(r"[^0-9]", "", my_string)
    arr = []
    for i in answer :
        arr.append(int(i))
    return sorted(arr)