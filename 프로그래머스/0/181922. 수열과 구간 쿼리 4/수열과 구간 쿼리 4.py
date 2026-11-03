def solution(arr, queries):
    answer = []
    for query in queries:
        print(query)
        for i in range(query[0],query[1]+1):
            if query[2]==0:
                if i==0:
                    arr[0]+=1
                
            elif i%query[2]==0:
                arr[i]+=1
    return arr