#알파벳 대문자 upper() 
s=input().upper()

#A~Z 26개 리스트 생성
cnt_list=[0]*26
for char in s:
   index=ord(char)-ord('A') #A-0, B-1 ...
   cnt_list[index]+=1

# .couunt 메소드
max_count=max(cnt_list)
if cnt_list.count(max_count)>1: #최대값이 여러개면 ?
   print("?")
else:
   #.index() - 리스트 안에서 값이 처음 나오는 위치 반환
   max_index=cnt_list.index(max_count) #최대값 위치 인덱스 
   print(chr(max_index+ord('A'))) #인덱스 -> 문자 변환