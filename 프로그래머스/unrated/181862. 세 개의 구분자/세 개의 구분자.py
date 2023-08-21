import re
def solution(myStr):
    answer = ' '.join(re.split(r'a|b|c', myStr)).split()
    return answer if len(answer) > 0 else ["EMPTY"]