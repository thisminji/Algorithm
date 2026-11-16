def solution(myString):
    answer = ''
    myString= myString.lower()
    
    for i in myString:
        if i=='a':
            myString=myString.replace('a','A')
        
    return myString