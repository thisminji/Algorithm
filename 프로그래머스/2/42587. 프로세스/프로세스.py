def solution(priorities, location):
    queue=[]
    answer=0
    
    for i in range(len(priorities)):
        queue.append([priorities[i],i])
    
    while queue:
        current=queue.pop(0)
        
        max_num=0
        for i in queue:
            if i[0]>max_num:
                max_num=i[0]
        if current[0]<max_num:
            queue.append(current)
        else:
            answer+=1
            
            if current[1]==location:
                return answer