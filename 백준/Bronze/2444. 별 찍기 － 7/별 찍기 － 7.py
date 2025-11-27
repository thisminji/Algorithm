n=int(input())
# 공백 : 줄번호 - 1
# * : 2*줄번호 -1
#n=5
# i  공백 *
# i=1 4 1
# I=2 3 3
# i=3 2 5
# i=4 1 7
# i=5 0 9

for i in range(1,n+1): #n줄
   space = ' ' * (n - i)
   star = '*' * (2 * i - 1)
   print(space + star)

for i in range(n-1,0,-1):
   space = ' ' * (n - i)
   star = '*' * (2 * i - 1)
   print(space + star)