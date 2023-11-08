def solution(progresses, speeds):
    from collections import deque

    answer = []
    count = 0
    days = 0
    queue = deque()

    for i in range(len(progresses)):
        queue.append((progresses[i], speeds[i]))

    while queue:
        if ((queue[0][0]+ days * queue[0][1]) >=100 ):
            progresses , speeds = queue.popleft()
            count +=1
        else :
            if count > 0 :
                answer.append(count)
                count =0
            else:
                days +=1
    answer.append(count)
    return answer

progresses =[93, 30, 55]
speeds =[1, 30, 5]
print(solution(progresses,speeds))
