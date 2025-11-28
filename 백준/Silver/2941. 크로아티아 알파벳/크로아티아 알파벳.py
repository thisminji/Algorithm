s=input()

# List of Croatian alphabet combinations
cro=['c=','c-','dz=','d-','lj','nj','s=','z=']

for i in cro:
#문자열 불변이라서 바뀐 새 문자열 반환
#replace(바꿀문자,바꿀문자열)
   s=s.replace(i,'*')
print(len(s))