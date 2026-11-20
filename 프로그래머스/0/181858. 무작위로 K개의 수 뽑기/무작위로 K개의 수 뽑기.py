def solution(arr, k):
    answer = []
    for i in range(len(arr)):
        if arr[i] not in answer:
            answer.append(arr[i])
    print(answer)
     
    for i in range(k-len(answer)):
        answer.append(-1)
        
    return answer[:k]