def solution(arr):
    row=len(arr)
    col=len(arr[0])
    if row>col:
        for i in arr:
            i.extend([0]*(row-col))
    elif row<col:
        for i in range(col-row):
            arr.append([0] * col)            
    return arr