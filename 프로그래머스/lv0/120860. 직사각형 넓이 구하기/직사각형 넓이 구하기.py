def solution(dots):
    x1, x2 = max(dots)
    y1, y2 = min(dots)
    
    return (x1-y1) * (x2-y2)