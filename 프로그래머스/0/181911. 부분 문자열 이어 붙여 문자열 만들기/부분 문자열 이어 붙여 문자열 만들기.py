def solution(my_strings, parts):
    answer = ''
    i=0
    for part in parts:
        print(part)
        answer+=my_strings[i][part[0]:part[1]+1]
        i+=1
    return answer