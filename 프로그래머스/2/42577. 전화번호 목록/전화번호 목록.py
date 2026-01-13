def solution(phone_book):
    phone_book.sort()
    
    for i in range(len(phone_book)-1):
        # 문자열.startswith(시작하는지_확인할_문자열)
        if phone_book[i+1].startswith(phone_book[i]):
            return False
    return True
