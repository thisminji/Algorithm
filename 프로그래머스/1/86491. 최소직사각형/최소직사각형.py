def solution(sizes):
    max_list=[]
    min_list=[]
    
    for i in sizes:
        max_list.append(max(i))
        min_list.append(min(i))

    return max(max_list)*max(min_list)