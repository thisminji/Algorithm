def solution(todo_list, finished):
    answer = []
    for idx, word in enumerate(todo_list):
        if finished[idx]==False:
            answer.append(word)
    return answer
