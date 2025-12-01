words=[input() for _ in range(5)]

result=''

#가장 긴 줄의 길이 
max_len=max(len(row) for row in words)

#세로 읽기
for col in range(max_len):
    for row in range(5):
        #현재 줄(words[row])에 col번째 글자가 있을 때만 추가      
        #col에 글자가 있으면
        if col < len(words[row]):
            result+=words[row][col]

print(result)