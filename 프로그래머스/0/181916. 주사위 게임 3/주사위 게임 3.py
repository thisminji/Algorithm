def solution(a, b, c, d):

    count = {}

    dice = [a, b, c, d]

    answer = 0

    for i in dice:
        count[i] = count.get(i, 0) + 1
    if len(count) == 1:
        answer = 1111 * list(count.keys())[0]

    elif len(count) == 2:
        p, q = list(count.keys())
        if count[p] == 3:
            answer = (10 * p + q) ** 2
        elif count[q] == 3:
            answer = (10 * q + p) ** 2
        else:
            answer = (p + q) * abs(p - q)
    elif len(count) == 3:
        numbers = []

        for key, value in count.items():
            if value == 1:
                numbers.append(key)
        answer = numbers[0] * numbers[1]
    else:
        answer = min(dice)
    return answer