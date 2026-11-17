def solution(str_list):
    for i, word in enumerate(str_list):
        if word=='l':
            return str_list[:i]
        elif word=='r':
            return str_list[i+1:]
    return []