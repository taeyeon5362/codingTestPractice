def solution(score):
    answer1 = []
    for i in score :
        answer1.append(sum(i))
    answer2 = sorted(answer1, reverse = True)
    return [answer2.index(s) + 1 for s in answer1]