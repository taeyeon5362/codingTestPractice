def solution(myString):
    myString = myString.split('x')
    myString = ' '.join(myString).split()
    return sorted(myString)


