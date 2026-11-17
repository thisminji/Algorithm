def solution(array, n):
    diff=[]
    array.sort()
    for i in array:
        diff.append(abs(i-n))
    print(diff)
    print(min(diff))
    print(diff.index(min(diff)))
    print(array[diff.index(min(diff))])
    return array[diff.index(min(diff))]