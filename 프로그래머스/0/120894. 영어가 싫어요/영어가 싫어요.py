def solution(numbers):
    words=["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine" ]
    
    for idx, word in enumerate(words):
        numbers=numbers.replace(word,str(idx))
    return int(numbers)