def solution(progresses, speeds):
    answer = []
    while progresses :
        count = 0
        
        while progresses and progresses[0] >= 100 :
            count += 1
            progresses.pop(0)
            speeds.pop(0)
            
        progresses = [progresses[i] + speeds[i] for i in range(len(progresses))]
        
        if count :
            answer.append(count)
    return answer