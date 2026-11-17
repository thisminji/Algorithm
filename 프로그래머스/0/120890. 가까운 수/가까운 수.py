def solution(array, n):
    diff=[]
    array.sort()
    for i in array:
        diff.append(abs(i-n))
    return array[diff.index(min(diff))]