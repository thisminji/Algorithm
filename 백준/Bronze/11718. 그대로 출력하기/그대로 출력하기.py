while True:
   try:
      s=input()
      print(s)
   # 더 이상 입력이 없으면
   #End Of File
   except EOFError: 
   # 반복종료
      break