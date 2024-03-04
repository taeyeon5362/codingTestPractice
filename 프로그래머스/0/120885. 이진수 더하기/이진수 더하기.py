def solution(bin1, bin2):
    bin1 = '0b' + bin1
    bin2 = '0b' + bin2
    num1 = int(bin1,2)
    num2 = int(bin2,2)
    answer = bin(num1 + num2)
    return answer[2:]