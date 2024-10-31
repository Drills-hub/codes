def solution(money):
    answer = []
    coffee = money // 5500
    change = money % 5500
    answer.append(coffee)
    answer.append(change)
    return answer