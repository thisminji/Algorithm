def solution(sizes):
    max_w=0
    max_h=0
    
    for w, h in sizes:
        big =max(w,h)
        small=min(w,h)
        
        if big>max_w:
            max_w=big
            
        if small>max_h:
            max_h=small
    answer = max_w*max_h
    return answer