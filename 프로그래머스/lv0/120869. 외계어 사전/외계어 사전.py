def solution(spell, dic):
    for i in dic :
        if ''.join(sorted(spell)) == ''.join(sorted(i)) :
            return 1
    return 2
        