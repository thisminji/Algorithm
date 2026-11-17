def solution(todo_list, finished):
    answer = []
    for idx, word in enumerate(todo_list):
        if not finished[idx]:
            answer.append(word)
    return answer
