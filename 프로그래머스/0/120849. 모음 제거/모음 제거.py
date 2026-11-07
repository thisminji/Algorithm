def solution(my_string):
    answer = ''
    remove=['a','e','i','o','u']
    
    for i in my_string:
        if i not in remove:
            answer+=i     
    return answer