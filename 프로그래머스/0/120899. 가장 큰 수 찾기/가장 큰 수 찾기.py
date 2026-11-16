def solution(array):
    max_num=max(array)
    idx=array.index(max_num)
    return [max_num,idx]