def solution(a, b, c, d) :
    arr1 = list(set([a,b,c,d]))
    arr2 = [a,b,c,d]
    counter = {}
    for i in arr2 :
        try : counter[i] += 1
        except : counter[i] = 1
        
    if len(arr1) == 1 :
        return a * 1111
    elif len(arr1) == 4 :
        return min(arr2)
    elif len(arr1) == 3 :
        arr3 = []
        for key, value in counter.items():
            if value == 1 :
                arr3.append(key)
        return arr3[0] * arr3[1]
    else :
        arr4 = []
        arr5 = []
        arr6 = []
        for key, value in counter.items():
            if value == 2 :
                arr4.append(key)
            elif value == 3 :
                arr5.append(key)
            elif value == 1 :
                arr6.append(key)
        if len(arr4) != 0 :
            return (arr4[0] + arr4[1]) * abs(arr4[0] - arr4[1]) 
        if len(arr5) != 0 :
            return (10 * arr5[0] + arr6[0]) ** 2