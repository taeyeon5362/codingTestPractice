import math

def solution(numer1, denom1, numer2, denom2):
    mo = denom1 * denom2
    ja = numer1 * denom2 + numer2 * denom1
    
    gcd_value = math.gcd(mo, ja)
    
    answer = [ja / gcd_value, mo / gcd_value]
    
    return answer