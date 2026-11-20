def solution(arr):
    num=1
    while num<len(arr):
        num*=2
    for i in range(num-len(arr)):
        arr.append(0)
    return arr