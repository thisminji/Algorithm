def solution(brown, yellow):
    for i in range(1,yellow+1):
        if yellow%i==0:
            w=yellow//i+2
            h=i+2
        if w>=h and w*h-yellow==brown:
            return [w,h]