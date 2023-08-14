def solution(myString):
    myString = ' '.join(myString.split('x')).split()
    return sorted(myString)


